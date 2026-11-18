/* =========================================================
   Minh Ngo — Portfolio Box · real-time 3D desk
   ---------------------------------------------------------
   Every 3D object follows the HTML element it replaces:
   each frame we read that element's position, rotation,
   scale and opacity (including the CSS animations for the
   box drop, lid lift, hovers and clicks) and place the mesh
   so its top face lands exactly where the artwork was.
   Hit areas, labels and text stay in HTML, so clicks and
   positions are unchanged. If WebGL is unavailable the
   original images stay visible.
   ========================================================= */

import * as THREE from 'three';
import { RoundedBoxGeometry } from 'three/addons/geometries/RoundedBoxGeometry.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';

const done = (ok) => window.__scene3dDone?.(ok);
const stage = document.getElementById('stage');

// design frame: 1440 × 900, or 1080 × 2160 on phones held upright
const PORTRAIT = document.documentElement.classList.contains('is-portrait');
const W = PORTRAIT ? 1080 : 1440;
const H = PORTRAIT ? 2160 : 900;
const D = 1800; // camera height above the desk, in design px
const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ---------- palette ---------- */
const C = {
  desk: 0x16171b,
  ink: 0x0d0e11,
  black: 0x141518,
  graphite: 0x23252b,
  alu: 0xb9bdc4,
  aluDark: 0x6c717a,
  paper: 0xf1eee8,
  accent: 0xff5a1f,
  white: 0xf4f4f2,
};

/* ---------- renderer ---------- */
let renderer;
try {
  const probe = document.createElement('canvas');
  if (!(probe.getContext('webgl2') || probe.getContext('webgl'))) throw new Error('no webgl');
  renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: 'high-performance' });
} catch (e) {
  done(false);
  throw e;
}
{
  const gl = renderer.getContext();
  const info = gl.getExtension('WEBGL_debug_renderer_info');
  const name = info ? String(gl.getParameter(info.UNMASKED_RENDERER_WEBGL)) : '';
  if (/swiftshader|llvmpipe|software/i.test(name) && !new URLSearchParams(location.search).has('force3d')) {
    renderer.dispose();
    done(false);
    throw new Error('software WebGL: keeping the illustrated desk');
  }
}
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.05;
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.setClearColor(C.desk);
const canvas = renderer.domElement;
canvas.className = 'scene3d';
canvas.setAttribute('aria-hidden', 'true');
stage.prepend(canvas);
const vignette = document.createElement('div');
vignette.className = 'scene-vignette';
canvas.after(vignette);

let needsDraw = true;
// the canvas covers the whole window (in stage units), so the desk carries on
// past the 1440 × 900 frame on wide or tall screens instead of stopping short
const vis = { x: 0, y: 0, w: W, h: H };
function resize() {
  needsDraw = true;
  const v = window.__stageView;
  if (v) {
    vis.x = -v.x / v.s;
    vis.y = -v.y / v.s;
    vis.w = v.vw / v.s;
    vis.h = v.vh / v.s;
  }
  for (const el of [canvas, vignette]) {
    Object.assign(el.style, { left: `${vis.x}px`, top: `${vis.y}px`, width: `${vis.w}px`, height: `${vis.h}px` });
  }
  const s = v ? v.s : stage.getBoundingClientRect().width / W || 1;
  const pr = Math.min((window.devicePixelRatio || 1) * s, 2 * s, 3200 / vis.w);
  renderer.setPixelRatio(pr);
  renderer.setSize(vis.w, vis.h, false);
}
addEventListener('stagefit', resize);
addEventListener('resize', resize);
resize();

const maxAniso = renderer.capabilities.getMaxAnisotropy();

/* ---------- scene, light, camera ---------- */
const scene = new THREE.Scene();
const pmrem = new THREE.PMREMGenerator(renderer);
scene.environment = pmrem.fromScene(new RoomEnvironment(renderer), 0.04).texture;

const key = new THREE.DirectionalLight(0xfff4e8, 2.6);
key.position.set(W / 2 - 760, -H / 2 + 880, 1500);
key.target.position.set(W / 2, -H / 2, 0);
key.castShadow = true;
key.shadow.mapSize.setScalar(Math.min(innerWidth, innerHeight) < 700 ? 2048 : 4096);
Object.assign(key.shadow.camera, PORTRAIT
  ? { left: -900, right: 900, top: 1350, bottom: -1350, near: 200, far: 4200 }
  : { left: -1150, right: 1150, top: 900, bottom: -900, near: 200, far: 4200 });
key.shadow.bias = -0.0004;
key.shadow.normalBias = 0.6;
key.shadow.radius = 4;
scene.add(key, key.target);

const fill = new THREE.DirectionalLight(0x9fb6ff, 0.45);
fill.position.set(W / 2 + 900, -H / 2 - 700, 900);
fill.target.position.set(W / 2, -H / 2, 0);
scene.add(fill, fill.target);
scene.add(new THREE.HemisphereLight(0xdfe6ff, 0x1a1410, 0.35));

const cam = new THREE.PerspectiveCamera();
cam.near = 40;
cam.far = D + 400;
const cam0 = new THREE.Vector2(W / 2, -H / 2);
const camPos = cam0.clone();
const camGoal = cam0.clone();

// off-axis projection: the desk plane (z = 0) always maps exactly onto the
// 1440 × 900 stage, wherever the camera moves — only things with height shift
function placeCamera() {
  cam.position.set(camPos.x, camPos.y, D);
  cam.updateMatrixWorld();
  const k = cam.near / D;
  cam.projectionMatrix.makePerspective(
    (vis.x - camPos.x) * k,
    (vis.x + vis.w - camPos.x) * k,
    (-vis.y - camPos.y) * k,
    (-(vis.y + vis.h) - camPos.y) * k,
    cam.near,
    cam.far,
  );
  cam.projectionMatrixInverse.copy(cam.projectionMatrix).invert();
}

/* ---------- helpers ---------- */
function tex(w, h, draw, { repeat, srgb = true } = {}) {
  const c = document.createElement('canvas');
  c.width = w;
  c.height = h;
  draw(c.getContext('2d'), w, h);
  const t = new THREE.CanvasTexture(c);
  if (srgb) t.colorSpace = THREE.SRGBColorSpace;
  t.anisotropy = maxAniso;
  if (repeat) {
    t.wrapS = t.wrapT = THREE.RepeatWrapping;
    t.repeat.set(repeat[0], repeat[1]);
  }
  return t;
}

function noise(size, base, spread, alpha = 1) {
  return (g) => {
    const img = g.createImageData(size, size);
    for (let i = 0; i < img.data.length; i += 4) {
      const v = base + (Math.random() - 0.5) * spread;
      img.data[i] = img.data[i + 1] = img.data[i + 2] = v;
      img.data[i + 3] = 255 * alpha;
    }
    g.putImageData(img, 0, 0);
  };
}

const mat = (color, o = {}) =>
  new THREE.MeshPhysicalMaterial({
    color,
    roughness: o.r ?? 0.5,
    metalness: o.m ?? 0,
    clearcoat: o.cc ?? 0,
    clearcoatRoughness: o.ccr ?? 0.25,
    map: o.map ?? null,
    roughnessMap: o.rmap ?? null,
    envMapIntensity: o.env ?? 0.7,
    transparent: !!o.transparent,
    opacity: o.opacity ?? 1,
    side: o.side ?? THREE.FrontSide,
    iridescence: o.irid ?? 0,
  });

function rrShape(w, h, r, cx = 0, cy = 0) {
  const s = new THREE.Shape();
  const x = cx - w / 2;
  const y = cy - h / 2;
  r = Math.max(0.01, Math.min(r, w / 2, h / 2));
  s.moveTo(x + r, y);
  s.lineTo(x + w - r, y);
  s.quadraticCurveTo(x + w, y, x + w, y + r);
  s.lineTo(x + w, y + h - r);
  s.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
  s.lineTo(x + r, y + h);
  s.quadraticCurveTo(x, y + h, x, y + h - r);
  s.lineTo(x, y + r);
  s.quadraticCurveTo(x, y, x + r, y);
  return s;
}

// flat UVs across the top face so a texture fills the outline exactly
function planarUV(g) {
  g.computeBoundingBox();
  const { min, max } = g.boundingBox;
  const p = g.attributes.position;
  const uv = g.attributes.uv;
  for (let i = 0; i < p.count; i++) {
    uv.setXY(i, (p.getX(i) - min.x) / (max.x - min.x), (p.getY(i) - min.y) / (max.y - min.y));
  }
  uv.needsUpdate = true;
  return g;
}

// extruded outline, bottom at z = 0, softly bevelled edges
function extrude(shape, d, bev = 1.5, curve = 12) {
  const b = Math.min(bev, d / 2 - 0.05);
  const g = new THREE.ExtrudeGeometry(shape, {
    depth: Math.max(d - 2 * b, 0.05),
    bevelEnabled: b > 0,
    bevelThickness: b,
    bevelSize: b,
    bevelOffset: -b,
    bevelSegments: 3,
    curveSegments: curve,
  });
  g.translate(0, 0, b);
  return planarUV(g);
}

const slab = (w, h, d, r, bev, cx, cy) => extrude(rrShape(w, h, r, cx, cy), d, bev);

function poly(pts) {
  const s = new THREE.Shape();
  pts.forEach(([x, y], i) => (i ? s.lineTo(x, y) : s.moveTo(x, y)));
  s.closePath();
  return s;
}

// cylinder standing on the desk (axis = z), bottom at z = 0
const cylZ = (rt, rb, h, seg = 48) => new THREE.CylinderGeometry(rt, rb, h, seg).rotateX(Math.PI / 2).translate(0, 0, h / 2);

function add(group, geo, material, o = {}) {
  const m = new THREE.Mesh(geo, material);
  m.position.set(o.x ?? 0, o.y ?? 0, o.z ?? 0);
  if (o.rz) m.rotation.z = o.rz;
  if (o.rx) m.rotation.x = o.rx;
  if (o.ry) m.rotation.y = o.ry;
  m.castShadow = o.cast ?? true;
  m.receiveShadow = true;
  group.add(m);
  return m;
}

const rad = THREE.MathUtils.degToRad;

/* art-local coordinates: (x, y) in px from the artwork's top-left, y down */
const local = (iw, ih) => (x, y) => [x - iw / 2, ih / 2 - y];

/* ---------- shared textures ---------- */
const FONT = '"Bricolage Grotesque", "Inter", system-ui, sans-serif';

const deskTex = tex(512, 512, noise(512, 232, 26), { repeat: [7, 5] });
const feltTex = tex(256, 256, noise(256, 225, 50), { repeat: [10, 6] });
const leatherTex = tex(256, 256, (g, w, h) => {
  noise(256, 210, 70)(g);
  g.globalAlpha = 0.25;
  for (let i = 0; i < 900; i++) {
    g.fillStyle = Math.random() > 0.5 ? '#fff' : '#000';
    g.beginPath();
    g.arc(Math.random() * w, Math.random() * h, Math.random() * 1.6 + 0.4, 0, 7);
    g.fill();
  }
}, { repeat: [3, 2] });

/* =========================================================
   Object builders — each returns { group, zt }
   zt = height of the face the HTML text/labels sit on
   ========================================================= */

function buildDesk() {
  const g = new THREE.Group();
  const m = mat(C.desk, { r: 0.92, map: deskTex, env: 0.35 });
  add(g, new THREE.PlaneGeometry(6000, 4000), m, { x: W / 2, y: -H / 2, cast: false });
  return g;
}

function buildMonitor(iw, ih) {
  const g = new THREE.Group();
  const L = local(iw, ih);
  const P = (pts) => pts.map(([x, y]) => L(x, y));
  const shell = mat(C.alu, { r: 0.32, m: 0.85, env: 1 });
  const bezel = mat(0x07080a, { r: 0.25, cc: 1, env: 0.8 });
  // aluminium back shell and chin
  add(g, extrude(poly(P([[20, -60], [1232, -60], [1078, 352], [174, 352]])), 44, 3), shell);
  // black glass front with a thin bezel
  add(g, extrude(poly(P([[27, -60], [1225, -60], [1071, 318], [181, 318]])), 4, 1), bezel, { z: 44 });
  const screenTex = tex(1024, 512, (c, w, h) => {
    const gr = c.createLinearGradient(0, 0, 0, h);
    gr.addColorStop(0, '#121726');
    gr.addColorStop(1, '#0b0d14');
    c.fillStyle = gr;
    c.fillRect(0, 0, w, h);
    const glow = c.createRadialGradient(w * 0.5, h * 1.1, 10, w * 0.5, h * 1.1, w * 0.6);
    glow.addColorStop(0, 'rgba(255,90,31,0.18)');
    glow.addColorStop(1, 'rgba(255,90,31,0)');
    c.fillStyle = glow;
    c.fillRect(0, 0, w, h);
  });
  const screen = new THREE.MeshPhysicalMaterial({ color: 0xffffff, map: screenTex, roughness: 0.18, clearcoat: 1, envMapIntensity: 0.5 });
  add(g, extrude(poly(P([[44, -60], [1208, -60], [1062, 306], [190, 306]])), 0.6, 0), screen, { z: 48 });
  // stand foot on the desk: kept short so it ends in front of the box's
  // back wall instead of running underneath it
  add(g, slab(250, 24, 9, 10, 3, ...L(625.5, 364)), shell);
  return { group: g, zt: 48.6 };
}

function buildTea(iw, ih) {
  const g = new THREE.Group();
  const L = local(iw, ih);
  const [cx, cy] = L(140, 138);
  add(g, cylZ(116, 112, 9, 96), mat(C.graphite, { r: 0.35, cc: 0.6 }), { x: cx, y: cy });
  // ceramic cup: a lathe profile with a rolled rim
  const prof = [[0, 0], [78, 0], [92, 4], [101, 22], [106, 58], [107, 64], [103, 66], [98, 60], [95, 30], [86, 12], [0, 12]].map(([x, y]) => new THREE.Vector2(x, y));
  const cup = new THREE.LatheGeometry(prof, 96).rotateX(Math.PI / 2);
  add(g, cup, mat(0xefede8, { r: 0.28, cc: 0.8, env: 0.9 }), { x: cx, y: cy, z: 9 });
  const matcha = tex(512, 512, (c, w) => {
    const gr = c.createRadialGradient(w / 2, w / 2, 10, w / 2, w / 2, w / 2);
    gr.addColorStop(0, '#c7d77a');
    gr.addColorStop(0.55, '#9bb453');
    gr.addColorStop(1, '#5f7a2c');
    c.fillStyle = gr;
    c.fillRect(0, 0, w, w);
    const foam = c.createRadialGradient(w * 0.46, w * 0.44, 4, w / 2, w / 2, w / 2);
    foam.addColorStop(0, 'rgba(236,242,200,0.55)');
    foam.addColorStop(0.6, 'rgba(236,242,200,0.12)');
    foam.addColorStop(1, 'rgba(236,242,200,0)');
    c.fillStyle = foam;
    c.fillRect(0, 0, w, w);
    for (let i = 0; i < 260; i++) {
      const a = Math.random() * Math.PI * 2;
      const d = Math.sqrt(Math.random()) * w * 0.47;
      c.fillStyle = `rgba(240,245,215,${0.08 + Math.random() * 0.18})`;
      c.beginPath();
      c.arc(w / 2 + Math.cos(a) * d, w / 2 + Math.sin(a) * d, 1 + Math.random() * 3.5, 0, 7);
      c.fill();
    }
  });
  add(g, new THREE.CircleGeometry(96, 96), mat(0xffffff, { map: matcha, r: 0.25, cc: 1, ccr: 0.05 }), { x: cx, y: cy, z: 9 + 58, cast: false });
  // handle, toward the lower right like the drawing
  const hd = new THREE.Vector2(0.62, -0.78).normalize();
  const handle = add(g, new THREE.TorusGeometry(22, 7, 16, 40, Math.PI).rotateZ(-Math.PI / 2).rotateX(Math.PI / 2), mat(0xefede8, { r: 0.28, cc: 0.8 }), {
    x: cx + hd.x * 100, y: cy + hd.y * 100, z: 9 + 34,
  });
  handle.rotation.z = Math.atan2(hd.y, hd.x);
  // two tea leaves
  const leaf = new THREE.Shape();
  leaf.moveTo(0, 0);
  leaf.quadraticCurveTo(24, 22, 62, 0);
  leaf.quadraticCurveTo(24, -22, 0, 0);
  const leafMat = mat(0x4f7a32, { r: 0.45, cc: 0.4 });
  const l1 = add(g, extrude(leaf, 3, 0.8), leafMat, { x: L(22, 250)[0], y: L(22, 250)[1], z: 9 });
  l1.rotation.z = rad(18);
  const l2 = add(g, extrude(leaf, 3, 0.8), leafMat, { x: L(236, 112)[0], y: L(236, 112)[1], z: 9 });
  l2.rotation.z = rad(-70);
  return { group: g, zt: 75 };
}

function buildPencil(iw, ih) {
  const g = new THREE.Group();
  const r = 12;
  const seg = (y0, y1, rt, rb, m, sides = 6) => {
    const h = y1 - y0;
    add(g, new THREE.CylinderGeometry(rt, rb, h, sides), m, { y: ih / 2 - (y0 + y1) / 2, z: r });
  };
  seg(0, 20, r * 0.92, r * 0.92, mat(0x2a2a2e, { r: 0.8 }), 24);
  seg(20, 36, r, r, mat(C.alu, { r: 0.3, m: 0.9 }), 24);
  seg(36, 344, r, r, mat(C.accent, { r: 0.42, cc: 0.5 }));
  seg(344, 384, r, 3.6, mat(0xd8b48a, { r: 0.8 }));
  seg(384, 395, 3.6, 0.5, mat(0x2b2b2e, { r: 0.5, m: 0.4 }));
  return { group: g, zt: r * 2 };
}

function buildPen(iw, ih) {
  const g = new THREE.Group();
  const r = 10;
  const seg = (y0, y1, rt, rb, m) => add(g, new THREE.CylinderGeometry(rt, rb, y1 - y0, 32), m, { y: ih / 2 - (y0 + y1) / 2, z: r });
  const silver = mat(0xd5d8dd, { r: 0.22, m: 1, env: 1 });
  seg(0, 6, r * 0.7, r, silver);
  seg(6, 186, r, r, silver);
  seg(186, 286, r * 0.96, r * 0.96, mat(0x1b1c20, { r: 0.75 }));
  seg(286, 318, r * 0.96, 4, silver);
  seg(318, 339, 4, 0.8, mat(0x1b1c20, { r: 0.4, m: 0.6 }));
  // pocket clip
  add(g, new RoundedBoxGeometry(5, 120, 4, 2, 2), silver, { y: ih / 2 - 70, z: r * 2 });
  return { group: g, zt: r * 2 };
}

function buildGreenbook(iw, ih) {
  const g = new THREE.Group();
  const L = local(iw, ih);
  const book = new THREE.Group();
  const [bx, by] = L(186.4, 228.6);
  book.position.set(bx, by, 0);
  book.rotation.z = rad(66);
  g.add(book);
  const len = 390;
  const wid = 227;
  const cover = mat(0x3d5a45, { r: 0.7, map: leatherTex, env: 0.5 });
  add(book, slab(len, wid - 8, 10, 8, 2, 0, -4), mat(0xe9e4d8, { r: 0.9 }));
  add(book, slab(len, wid - 8, 4, 8, 1.2, 0, -4), cover, { z: 10 });
  // wire spiral along the top edge
  const wire = mat(0xc9ccd2, { r: 0.25, m: 1 });
  for (let i = 0; i < 17; i++) {
    const ring = add(book, new THREE.TorusGeometry(8, 1.8, 8, 20), wire, { x: -len / 2 + 22 + i * 21.5, y: wid / 2 - 6, z: 7 });
    ring.rotation.y = Math.PI / 2;
  }
  // elastic band and label
  add(book, new RoundedBoxGeometry(len + 2, 12, 16, 2, 3), mat(0x1c1d21, { r: 0.6 }), { y: -wid / 2 + 30, z: 7 });
  const labelTex = tex(512, 160, (c, w, h) => {
    c.fillStyle = '#f2efe7';
    c.fillRect(0, 0, w, h);
    c.fillStyle = '#1d2a22';
    c.font = `600 64px ${FONT}`;
    c.textAlign = 'center';
    c.textBaseline = 'middle';
    c.letterSpacing = '10px';
    c.fillText('NOTEBOOK', w / 2, h / 2 + 4);
  });
  add(book, slab(112, 36, 0.6, 3, 0), mat(0xffffff, { map: labelTex, r: 0.8 }), { x: len / 2 - 96, y: 30, z: 14 });
  return { group: g, zt: 14 };
}

function buildPurplebook(iw, ih) {
  const g = new THREE.Group();
  const coverM = mat(0x4c1d33, { r: 0.65, map: leatherTex, env: 0.5 });
  add(g, slab(iw - 6, ih - 6, 18, 6, 1.5, -1, 0), mat(0xece6da, { r: 0.9 }));
  add(g, slab(iw, ih, 2.5, 9, 1), coverM);
  add(g, slab(iw, ih, 3.5, 9, 1.2), coverM, { z: 18.5 });
  // spine
  add(g, new RoundedBoxGeometry(14, ih, 24, 2, 6), coverM, { x: -iw / 2 + 7, z: 11 });
  // elastic closure in the accent colour
  add(g, new RoundedBoxGeometry(12, ih + 2, 24, 2, 4), mat(C.accent, { r: 0.55, cc: 0.3 }), { x: iw * 0.33, z: 11 });
  return { group: g, zt: 22 };
}

function buildAirpods(iw, ih) {
  const g = new THREE.Group();
  const L = local(iw, ih);
  const caseM = mat(C.white, { r: 0.18, cc: 1, ccr: 0.1, env: 0.9 });
  const body = new THREE.Group();
  const [x, y] = L(71.4, 67.3);
  body.position.set(x, y, 0);
  body.rotation.z = rad(63);
  g.add(body);
  add(body, new RoundedBoxGeometry(110, 102, 44, 8, 22), caseM, { z: 22 });
  add(body, new RoundedBoxGeometry(110.5, 2, 44.5, 2, 1), mat(0x9a9ca2, { r: 0.4 }), { y: 22, z: 22 });
  return { group: g, zt: 44 };
}

function buildBud(angle, cxArt, cyArt) {
  return (iw, ih) => {
    const g = new THREE.Group();
    const L = local(iw, ih);
    const bud = new THREE.Group();
    const [x, y] = L(cxArt, cyArt);
    bud.position.set(x, y, 0);
    bud.rotation.z = rad(-angle);
    g.add(bud);
    const m = mat(C.white, { r: 0.2, cc: 1, ccr: 0.1, env: 0.9 });
    add(bud, new THREE.CapsuleGeometry(7.5, 50, 6, 16).rotateZ(Math.PI / 2), m, { x: -10, z: 9 });
    add(bud, new THREE.SphereGeometry(19, 32, 24), m, { x: 20, z: 17 });
    add(bud, new THREE.SphereGeometry(5, 16, 12), mat(0x2b2d33, { r: 0.6 }), { x: 26, z: 33 });
    return { group: g, zt: 36 };
  };
}

function buildGlasses(iw, ih) {
  // wayfarer-style frames lying face up, arms folded underneath
  const g = new THREE.Group();
  const L = local(iw, ih);
  const frameM = mat(0x111215, { r: 0.22, cc: 1, ccr: 0.06, env: 0.9 });
  const metalM = mat(C.alu, { r: 0.25, m: 1 });
  const lensM = mat(0x2c3b40, { r: 0.04, cc: 1, ccr: 0.02, transparent: true, opacity: 0.55, env: 1.8, irid: 0.5 });
  // one rim outline in art px (left lens), mirrored for the right one
  const rimPts = (inset) => {
    const s = new THREE.Shape();
    const c = [84, 50];
    const pts = [
      [150, 9], [118, 5], [70, 4], [22, 6], // top edge, straight and strong
      [16, 14], [17, 34], [24, 62], [36, 84], [56, 96], [86, 99], [114, 95], [134, 84], [146, 64], [151, 38], [152, 18],
    ];
    const P = pts.map(([x, y]) => [c[0] + (x - c[0]) * (1 - inset / 70), c[1] + (y - c[1]) * (1 - inset / 48)]);
    return P;
  };
  const toShape = (P, mirror) => {
    const v = P.map(([x, y]) => new THREE.Vector2(...L(mirror ? 312 - x : x, y)));
    if (mirror) v.reverse();
    return new THREE.Shape(new THREE.SplineCurve([...v, v[0]]).getPoints(80));
  };
  for (const mirror of [false, true]) {
    const outer = toShape(rimPts(0), mirror);
    const inner = toShape(rimPts(12), mirror);
    outer.holes.push(new THREE.Path(inner.getPoints().reverse()));
    add(g, extrude(outer, 8, 1.6), frameM, { z: 10 });
    add(g, extrude(inner, 1.5, 0), lensM, { z: 13, cast: false });
    // hinge studs and the folded arm tucked under the lens
    const sx = mirror ? -1 : 1;
    const [hx, hy] = L(mirror ? 312 - 20 : 20, 12);
    add(g, new RoundedBoxGeometry(6, 6, 3, 1, 1), metalM, { x: hx + sx * 6, y: hy - 4, z: 19 });
    const [ax, ay] = L(mirror ? 312 - 84 : 84, 70);
    add(g, new RoundedBoxGeometry(136, 8, 7, 2, 3), frameM, { x: ax, y: ay, z: 4, rz: sx * rad(-6) });
  }
  // keyhole bridge
  const [bx, by] = L(156, 15);
  add(g, new RoundedBoxGeometry(22, 12, 8, 2, 3), frameM, { x: bx, y: by, z: 14 });
  return { group: g, zt: 18 };
}

function buildUsb(iw, ih) {
  const g = new THREE.Group();
  const L = local(iw, ih);
  const [x, y] = L(24.2, 65.2);
  add(g, new RoundedBoxGeometry(44, 96, 20, 4, 8), mat(0x101114, { r: 0.25, cc: 1 }), { x, y: y - 12, z: 10 });
  add(g, new RoundedBoxGeometry(28, 34, 10, 2, 1.5), mat(C.alu, { r: 0.25, m: 1 }), { x, y: y + 46, z: 6 });
  add(g, new RoundedBoxGeometry(4, 10, 2, 1, 0.8), mat(C.accent, { r: 0.4 }), { x, y: y + 20, z: 20.5 });
  return { group: g, zt: 20 };
}

function buildClip(iw, ih) {
  const g = new THREE.Group();
  const L = local(iw, ih);
  const [x, y] = L(21.5, 33.8);
  // binder clip: a black tapered spring body…
  const prof = new THREE.Shape();
  prof.moveTo(-13, -22.5);
  prof.lineTo(13, -22.5);
  prof.lineTo(13, 22.5);
  prof.lineTo(-13, 22.5);
  prof.closePath();
  add(g, extrude(prof, 14, 2.5), mat(0x101114, { r: 0.28, cc: 1, ccr: 0.15 }), { x, y });
  add(g, new RoundedBoxGeometry(10, 46, 4, 2, 1.5), mat(0x2a2c31, { r: 0.3, cc: 1 }), { x: x + 6, y, z: 14 });
  // …and two flat folded wire handles
  const wire = mat(0xd3d6db, { r: 0.18, m: 1, env: 1.1 });
  for (const [dy, len, z0] of [[0, 54, 3.2], [2, 48, 5.2]]) {
    const pts = [[6, 19], [26, 20], [len - 8, 12], [len, 0], [len - 8, -12], [26, -20], [6, -19]].map(
      ([px, py]) => new THREE.Vector3(x + px, y + py + dy, z0),
    );
    add(g, new THREE.TubeGeometry(new THREE.CatmullRomCurve3(pts), 48, 1.5, 8, false), wire);
  }
  return { group: g, zt: 16 };
}

function buildTray(iw, ih) {
  const g = new THREE.Group();
  const outer = rrShape(iw, ih, 100);
  outer.holes.push(rrShape(iw - 44, ih - 44, 80));
  const shell = mat(0x0b0c0e, { r: 0.6, cc: 0.3, ccr: 0.5, env: 0.5 });
  add(g, extrude(outer, 46, 3), shell);
  add(g, slab(iw - 30, ih - 30, 6, 86, 0), mat(0x2a2c33, { r: 1, map: feltTex, env: 0.2 }));
  return { group: g, zt: 6 };
}

function buildLid(iw, ih) {
  const g = new THREE.Group();
  const lidTex = tex(1838, 1134, (c, w, h) => {
    c.fillStyle = '#0d0e11';
    c.fillRect(0, 0, w, h);
    c.strokeStyle = 'rgba(255,255,255,0.08)';
    c.lineWidth = 3;
    const inset = 56;
    c.beginPath();
    c.roundRect(inset, inset, w - inset * 2, h - inset * 2, 150);
    c.stroke();
  });
  const top = mat(0xffffff, { map: lidTex, r: 0.72, cc: 0.25, ccr: 0.5, env: 0.45 });
  const side = mat(0x0b0c0e, { r: 0.6, cc: 0.3, ccr: 0.5, env: 0.5 });
  const geo = slab(iw + 6, ih + 6, 52, 103, 4);
  add(g, geo, [top, side]);
  return { group: g, zt: 52 };
}

function buildNote(iw, ih) {
  const g = new THREE.Group();
  const L = local(iw, ih);
  const [x, y] = L(138.3, 109.6);
  const paper = tex(820, 550, (c, w, h) => {
    c.fillStyle = '#ff6a2a';
    c.fillRect(0, 0, w, h);
    c.strokeStyle = 'rgba(0,0,0,0.10)';
    c.lineWidth = 3;
    for (let ly = 120; ly < h - 20; ly += 56) {
      c.beginPath();
      c.moveTo(30, ly);
      c.lineTo(w - 30, ly);
      c.stroke();
    }
  });
  add(g, slab(206, 138, 1.6, 3, 0.4), mat(0xffffff, { map: paper, r: 0.75, env: 0.4 }), { x, y: y, rz: rad(-1.5) });
  const tape = mat(0xf3efe6, { r: 0.6, transparent: true, opacity: 0.55 });
  add(g, slab(70, 22, 0.8, 1, 0), tape, { x: x - 92, y: y + 62, z: 1.6, rz: rad(38), cast: false });
  add(g, slab(70, 22, 0.8, 1, 0), tape, { x: x + 96, y: y + 66, z: 1.6, rz: rad(-12), cast: false });
  return { group: g, zt: 1.6 };
}

function buildPhone(iw, ih) {
  // same phone as the Apps popup (302 x 638, 50px corners), at 0.483 scale
  const g = new THREE.Group();
  const k = 146 / 302;
  const w = 302 * k;
  const h = 638 * k;
  const R = 50 * k; // outer corner radius
  const bez = 10 * k; // black bezel
  // graphite frame (the popup's thin #3a3d45 ring) and black glass front
  add(g, slab(w + 2, h + 2, 13, R + 1, 2.5), mat(0x3a3d45, { r: 0.3, m: 0.85, env: 1 }), { z: 1 });
  add(g, slab(w, h, 1.2, R, 0.6), mat(0x0b0c0f, { r: 0.2, cc: 1, env: 0.8 }), { z: 14.5 });
  // screen: same gradient as the popup, with the island
  const SW = 512;
  const SH = Math.round(SW * (618 / 282));
  const wall = tex(SW, SH, (c, cw, ch) => {
    const base = c.createLinearGradient(0, 0, 0, ch);
    base.addColorStop(0, '#14151b');
    base.addColorStop(1, '#090a0e');
    c.fillStyle = base;
    c.fillRect(0, 0, cw, ch);
    // radial-gradient(120% 70% at 15% 95%, ...)
    c.save();
    c.translate(cw * 0.15, ch * 0.95);
    c.scale(cw * 1.2, ch * 0.7);
    const gl = c.createRadialGradient(0, 0, 0, 0, 0, 1);
    gl.addColorStop(0, 'rgba(255, 90, 31, 0.55)');
    gl.addColorStop(0.4, 'rgba(184, 50, 26, 0.25)');
    gl.addColorStop(0.7, 'rgba(0, 0, 0, 0)');
    c.fillStyle = gl;
    c.fillRect(-2, -2, 4, 4);
    c.restore();
    const iW = (92 / 282) * cw;
    const iH = (26 / 618) * ch;
    c.fillStyle = '#000';
    c.beginPath();
    c.roundRect(cw / 2 - iW / 2, (12 / 618) * ch, iW, iH, iH / 2);
    c.fill();
  });
  add(g, slab(w - bez * 2, h - bez * 2, 0.4, R - bez, 0), new THREE.MeshPhysicalMaterial({ map: wall, roughness: 0.12, clearcoat: 1, envMapIntensity: 0.6 }), { z: 15.7, cast: false });
  return { group: g, zt: 16.1 };
}

function buildSwatch(iw, ih) {
  const g = new THREE.Group();
  const L = local(iw, ih);
  const [px, py] = L(156, 261);
  const sets = [
    { a: 36, cols: ['#0b3b38', '#0f5c55', '#11796f', '#14978a', '#2bb5a5', '#63d2c4', '#a9ebe2'] },
    { a: 17, cols: ['#5c0f22', '#8c1734', '#b81f45', '#e0335c', '#f05d7f', '#f792a8', '#fcc6d3'] },
    { a: 0, cols: ['#2a1360', '#3d1d8a', '#5228b5', '#6b3ddb', '#8a66ea', '#ad94f3', '#d4c6fa'] },
  ];
  sets.forEach(({ a, cols }, i) => {
    const t = tex(232, 992, (c, w, h) => {
      c.fillStyle = '#f2f0eb';
      c.fillRect(0, 0, w, h);
      const top = 14;
      const bh = (h - 190) / cols.length;
      cols.forEach((col, k) => {
        c.fillStyle = col;
        c.fillRect(12, top + k * bh, w - 24, bh - 10);
      });
      c.fillStyle = '#c9c6bf';
      for (let k = 0; k < 3; k++) c.fillRect(24, h - 150 + k * 22, 90 - k * 20, 8);
    });
    const strip = new THREE.Group();
    strip.position.set(px, py, i * 3.2);
    strip.rotation.z = rad(a);
    g.add(strip);
    add(strip, slab(58, 248, 3, 5, 0.6, 15, 104), mat(0xffffff, { map: t, r: 0.55, env: 0.5 }));
  });
  add(g, cylZ(7, 7, 12, 24), mat(C.alu, { r: 0.25, m: 1 }), { x: px, y: py });
  return { group: g, zt: 9.6 };
}

function buildFolder(iw, ih) {
  const g = new THREE.Group();
  const L = local(iw, ih);
  const [cx, cy] = L(154, 131);
  const w = 272;
  const h = 226;
  const back = new THREE.Shape();
  const x0 = cx - w / 2;
  const y0 = cy - h / 2;
  back.moveTo(x0 + 10, y0);
  back.lineTo(x0 + w - 10, y0);
  back.quadraticCurveTo(x0 + w, y0, x0 + w, y0 + 10);
  back.lineTo(x0 + w, y0 + h - 34);
  back.quadraticCurveTo(x0 + w, y0 + h - 24, x0 + w - 10, y0 + h - 24);
  back.lineTo(x0 + 104, y0 + h - 24);
  back.lineTo(x0 + 88, y0 + h - 8);
  back.quadraticCurveTo(x0 + 84, y0 + h, x0 + 76, y0 + h);
  back.lineTo(x0 + 10, y0 + h);
  back.quadraticCurveTo(x0, y0 + h, x0, y0 + h - 10);
  back.lineTo(x0, y0 + 10);
  back.quadraticCurveTo(x0, y0, x0 + 10, y0);
  add(g, extrude(back, 4, 1), mat(0x1f3b5c, { r: 0.6, env: 0.6 }));
  add(g, slab(w - 34, h - 48, 2, 4, 0.4, cx, cy - 6), mat(C.paper, { r: 0.9 }), { z: 4 });
  add(g, slab(w - 46, h - 60, 2, 4, 0.4, cx + 4, cy - 2), mat(0xe2ded5, { r: 0.9 }), { z: 6 });
  add(g, slab(w, h - 52, 5, 12, 1.2, cx, cy - 26), mat(0x2d5a8a, { r: 0.55, cc: 0.2, env: 0.6 }), { z: 8 });
  const label = tex(260, 120, (c, cw, ch) => {
    c.fillStyle = '#f4f2ec';
    c.fillRect(0, 0, cw, ch);
    c.fillStyle = '#9ba3ad';
    c.fillRect(26, 38, 170, 10);
    c.fillRect(26, 70, 120, 10);
  });
  add(g, slab(66, 30, 0.6, 3, 0, ...L(64, 112)), mat(0xffffff, { map: label, r: 0.85 }), { z: 13 });
  return { group: g, zt: 13 };
}

function buildCamera(iw, ih) {
  const g = new THREE.Group();
  const L = local(iw, ih);
  const [bx, by] = L(147.7, 100);
  const body = mat(0x17181b, { r: 0.75, map: leatherTex, env: 0.45 });
  const alu = mat(0xc7cbd1, { r: 0.28, m: 1, env: 1 });
  add(g, new RoundedBoxGeometry(266, 140, 56, 6, 12), body, { x: bx, y: by - 12, z: 28 });
  add(g, new RoundedBoxGeometry(266, 36, 62, 6, 10), alu, { x: bx, y: by + 64, z: 31 });
  add(g, new RoundedBoxGeometry(96, 26, 70, 4, 7), alu, { x: bx - 66, y: by + 82, z: 35 });
  add(g, new RoundedBoxGeometry(34, 14, 6, 2, 3), mat(0x0b0c0e, { r: 0.1, cc: 1 }), { x: bx - 66, y: by + 82, z: 70 });
  add(g, cylZ(10, 10, 8, 32), mat(C.accent, { r: 0.35, cc: 0.6 }), { x: bx + 104, y: by + 66, z: 62 });
  add(g, cylZ(13, 13, 5, 32), alu, { x: bx + 74, y: by + 66, z: 62 });
  // lens
  const [lx, ly] = L(182, 101);
  add(g, cylZ(70, 72, 16, 96), mat(0x24262b, { r: 0.4, m: 0.6 }), { x: lx, y: ly, z: 56 });
  add(g, cylZ(64, 66, 26, 96), mat(0x0e0f12, { r: 0.6, m: 0.3 }), { x: lx, y: ly, z: 72 });
  add(g, new THREE.TorusGeometry(64, 1.5, 8, 96), mat(C.accent, { r: 0.4 }), { x: lx, y: ly, z: 92 });
  add(g, cylZ(50, 52, 18, 96), mat(0x1a1b1f, { r: 0.35, m: 0.7 }), { x: lx, y: ly, z: 82 });
  add(g, new THREE.TorusGeometry(51, 1.6, 8, 96), alu, { x: lx, y: ly, z: 100 });
  add(g, new THREE.TorusGeometry(57, 1, 8, 96), alu, { x: lx, y: ly, z: 98 });
  const glass = mat(0x060914, { r: 0.03, cc: 1, ccr: 0.02, irid: 1, env: 1.4 });
  add(g, new THREE.SphereGeometry(46, 64, 32, 0, Math.PI * 2, 0, 0.62), glass, { x: lx, y: ly, z: 100 - 46 * Math.cos(0.62), rx: Math.PI / 2 });
  add(g, cylZ(16, 16, 2, 48), mat(0x05060a, { r: 0.05, cc: 1 }), { x: lx, y: ly, z: 99, cast: false });
  return { group: g, zt: 62 };
}

function buildIdcard(iw, ih) {
  const g = new THREE.Group();
  const L = local(iw, ih);
  const [tx, ty] = L(128.6, 115.8);
  add(g, slab(220, 130, 2, 10, 0.5), mat(0x124845, { r: 0.45, cc: 0.4 }), { x: tx, y: ty, rz: rad(-25.5) });
  const card = tex(1076, 520, (c, w, h) => {
    c.fillStyle = '#f5f4f0';
    c.fillRect(0, 0, w, h);
    c.fillStyle = '#ff5a1f';
    c.fillRect(0, 0, w, 76);
    c.fillStyle = '#16171b';
    c.beginPath();
    c.roundRect(48, 128, 200, 220, 18);
    c.fill();
    c.fillStyle = '#f5f4f0';
    c.beginPath();
    c.arc(148, 205, 38, 0, 7);
    c.fill();
    c.beginPath();
    c.ellipse(148, 330, 70, 56, 0, Math.PI, 0);
    c.fill();
    c.fillStyle = '#16171b';
    c.fillRect(300, 140, 500, 34);
    c.fillStyle = '#b9bcc4';
    c.fillRect(300, 205, 640, 18);
    c.fillRect(300, 245, 420, 18);
    for (let i = 0; i < 46; i++) c.fillRect(300 + i * 14, 296, i % 3 ? 4 : 8, 50);
    c.fillStyle = '#e4e2dc';
    c.beginPath();
    c.roundRect(48, 410, w - 96, 52, 26);
    c.fill();
  });
  const front = mat(0xffffff, { map: card, r: 0.4, cc: 0.6 });
  const edge = mat(0xe9e7e2, { r: 0.5 });
  const [fx, fy] = L(140, 112.2);
  add(g, slab(269, 130, 2.4, 10, 0.6), [front, edge], { x: fx, y: fy, z: 2 });
  return { group: g, zt: 4.4 };
}

function buildBrand(iw, ih) {
  const g = new THREE.Group();
  const t = tex(560, 560, (c, w) => {
    c.fillStyle = '#f4f1ea';
    c.fillRect(0, 0, w, w);
    c.strokeStyle = '#ff5a1f';
    c.lineWidth = 8;
    c.strokeRect(78, 78, w - 156, w - 156);
    c.fillStyle = '#fff';
    for (const [hx, hy] of [[78, 78], [w / 2, 78], [w - 78, 78], [78, w / 2], [w - 78, w / 2], [78, w - 78], [w / 2, w - 78], [w - 78, w - 78]]) {
      c.fillRect(hx - 18, hy - 18, 36, 36);
      c.strokeRect(hx - 18, hy - 18, 36, 36);
    }
    c.fillStyle = '#121316';
    c.font = `800 300px ${FONT}`;
    c.textAlign = 'center';
    c.textBaseline = 'middle';
    c.fillText('T', w / 2, w / 2 + 14);
  });
  add(g, slab(iw - 2, ih, 1.8, 3, 0.5), [mat(0xffffff, { map: t, r: 0.7, env: 0.5 }), mat(0xe6e2d8, { r: 0.8 })]);
  return { group: g, zt: 1.8 };
}

/* =========================================================
   Anchors: which HTML element each 3D object follows
   ========================================================= */
const BOOK_OFF = [44, 16];
const SPEC = [
  ['.monitor .art', buildMonitor],
  ['.tea .art', buildTea],
  ['.pencil .art', buildPencil],
  ['.greenbook .art', buildGreenbook],
  ['.pen .art', buildPen],
  // the purple book (and what sits on it) is nudged clear of the box wall
  ['.purplebook .art', buildPurplebook, 0, BOOK_OFF],
  ['.airpods .art', buildAirpods, 22, BOOK_OFF],
  ['.bud1 .art', buildBud(-42, 50.6, 50.1), 22, BOOK_OFF],
  ['.bud2 .art', buildBud(42, 50.6, 35.4), 22, BOOK_OFF],
  ['.glasses .art', buildGlasses],
  ['.usb .art', buildUsb],
  ['.clip1 .art', buildClip],
  ['.clip2 .art', buildClip],
  ['.clip3 .art', buildClip, 14],
  ['.tray', buildTray],
  ['.obj--phone .art', buildPhone, 6],
  ['.obj--swatch .art', buildSwatch, 6],
  ['.obj--folder .art', buildFolder, 6],
  ['.obj--camera .art', buildCamera, 6],
  ['.obj--idcard .art', buildIdcard, 6],
  ['.obj--brand .art', buildBrand, 6],
  ['#lid', buildLid],
  ['.note .art', buildNote, 52],
];

const items = [];

function matrixToStage(el) {
  let m = new DOMMatrix();
  let op = 1;
  for (let e = el; e && e !== stage; e = e.offsetParent) {
    if (e.offsetParent === null) return null;
    const cs = getComputedStyle(e);
    op *= parseFloat(cs.opacity);
    if (cs.visibility === 'hidden' && e !== el && !e.classList.contains('art')) op = 0;
    let t = new DOMMatrix().translate(e.offsetLeft, e.offsetTop);
    if (cs.transform && cs.transform !== 'none') {
      const [ox, oy] = cs.transformOrigin.split(' ').map(parseFloat);
      t = t.translate(ox, oy).multiply(new DOMMatrix(cs.transform)).translate(-ox, -oy);
    }
    m = t.multiply(m);
  }
  return { m, op };
}

function setup() {
  scene.add(buildDesk());
  for (const [sel, build, zb = 0, off = null] of SPEC) {
    const el = document.querySelector(sel);
    if (!el) continue;
    const iw = el.offsetWidth;
    const ih = el.offsetHeight;
    const { group, zt } = build(iw, ih);
    const root = new THREE.Group();
    root.add(group);
    scene.add(root);
    const mats = [];
    group.traverse((o) => {
      if (!o.isMesh) return;
      for (const m of [].concat(o.material)) {
        if (!mats.some((x) => x.m === m)) mats.push({ m, base: m.color.clone(), op: m.opacity, tr: m.transparent });
      }
    });
    const objEl = el.closest('.obj');
    items.push({ el, iw, ih, root, zb, zt, off, mats, hoverEl: objEl?.querySelector('.obj__hover'), hover: 0, alpha: -1 });
  }
}

/* ---------- per-frame sync ---------- */
function sync() {
  for (const it of items) {
    const r = matrixToStage(it.el);
    if (!r || r.op < 0.002) {
      it.root.visible = false;
      continue;
    }
    it.root.visible = true;
    const { m, op } = r;
    const p = m.transformPoint(new DOMPoint(it.iw / 2, it.ih / 2));
    if (it.off) {
      p.x += it.off[0];
      p.y += it.off[1];
    }
    const s = Math.hypot(m.a, m.b);
    const rot = Math.atan2(m.b, m.a);
    // a CSS scale-up reads as lifting toward the camera
    const lift = s > 1 ? D * (1 - 1 / s) : 0;
    const zSurf = it.zb + it.zt + lift;
    const k = (D - zSurf) / D;
    const g = s * k;
    it.root.position.set(camPos.x + (p.x - camPos.x) * k, camPos.y + (-p.y - camPos.y) * k, zSurf - it.zt * g);
    it.root.rotation.z = -rot;
    it.root.scale.setScalar(g);

    const hov = it.hoverEl ? parseFloat(getComputedStyle(it.hoverEl).opacity) || 0 : 0;
    const alpha = Math.round(op * 1000) / 1000;
    if (Math.abs(hov - it.hover) > 0.002 || alpha !== it.alpha) {
      it.hover = hov;
      it.alpha = alpha;
      const dim = 1 - 0.6 * hov;
      for (const x of it.mats) {
        x.m.color.copy(x.base).multiplyScalar(dim);
        const o = x.op * alpha;
        const tr = x.tr || alpha < 0.999;
        if (x.m.transparent !== tr) {
          x.m.transparent = tr;
          x.m.needsUpdate = true;
        }
        x.m.opacity = o;
      }
    }
  }
}

/* ---------- camera follows the pointer a little ---------- */
addEventListener('pointermove', (e) => {
  if (reduceMotion) return;
  const r = stage.getBoundingClientRect();
  const s = r.width / W;
  const nx = ((e.clientX - r.left) / s - W / 2) / (W / 2);
  const ny = ((e.clientY - r.top) / s - H / 2) / (H / 2);
  camGoal.set(cam0.x + Math.max(-1, Math.min(1, nx)) * 130, cam0.y - Math.max(-1, Math.min(1, ny)) * 90);
});

let lastSig = '';
function signature() {
  let sig = `${camPos.x.toFixed(2)},${camPos.y.toFixed(2)}`;
  for (const it of items) {
    const r = it.root;
    sig += r.visible ? `|${r.position.x.toFixed(2)},${r.position.y.toFixed(2)},${r.position.z.toFixed(2)},${r.rotation.z.toFixed(4)},${r.scale.x.toFixed(4)},${it.alpha},${it.hover.toFixed(3)}` : '|-';
  }
  return sig;
}

function frame() {
  camPos.lerp(camGoal, 0.06);
  if (camPos.distanceToSquared(camGoal) < 0.0004) camPos.copy(camGoal);
  placeCamera();
  sync();
  // skip the draw when nothing moved (saves battery while idle)
  const sig = signature();
  if (sig !== lastSig || needsDraw) {
    lastSig = sig;
    needsDraw = false;
    renderer.render(scene, cam);
  }
  requestAnimationFrame(frame);
}

(async () => {
  try {
    await Promise.race([document.fonts.ready, new Promise((r) => setTimeout(r, 1500))]);
    setup();
    placeCamera();
    sync();
    renderer.compile(scene, cam);
    renderer.render(scene, cam);
    // phones and tablets: time a few frames first; a slow GPU keeps the
    // illustrated desk instead of a stuttering 3D one
    if (matchMedia('(pointer: coarse)').matches && !new URLSearchParams(location.search).has('force3d')) {
      const gl = renderer.getContext();
      const px = new Uint8Array(4);
      const sync = () => gl.readPixels(0, 0, 1, 1, gl.RGBA, gl.UNSIGNED_BYTE, px);
      sync();
      const t0 = performance.now();
      for (let i = 0; i < 3; i++) renderer.render(scene, cam);
      sync();
      const perFrame = (performance.now() - t0) / 3;
      if (perFrame > 45) throw new Error(`slow GPU (${perFrame.toFixed(0)} ms a frame)`);
    }
    document.documentElement.classList.add('is-3d');
    done(true);
    requestAnimationFrame(frame);
  } catch (e) {
    console.error('3D scene failed, keeping the illustrated desk', e);
    canvas.remove();
    vignette.remove();
    done(false);
  }
})();
