# -*- coding: utf-8 -*-
import re

html_path = r"C:\Users\Pc\Downloads\minhngo-space\minhngo-space\index.html"
css_path = r"C:\Users\Pc\Downloads\minhngo-space\minhngo-space\minhngo-space\style.css"

# =========================================================================
# 1. ADD BULLETPROOF CSS FOR ABOUT CARD TO STYLE.CSS
# =========================================================================
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

about_card_css = """
/* =========================================================
   PERFECT ABOUT CARD LAYOUT (FLEXBOX / ZERO OVERLAP)
   ========================================================= */
.about.about-card {
  display: flex !important;
  flex-direction: column !important;
  height: 100% !important;
  position: absolute;
  inset: 0;
  overflow: hidden;
}
.about-card__head {
  height: 64px;
  background: var(--accent);
  color: #0d0e11;
  font-size: 28px;
  font-weight: 800;
  line-height: 64px;
  text-align: center;
  letter-spacing: -0.02em;
  flex: none;
  margin: 0 !important;
}
.about-card__body {
  flex: 1;
  padding: 20px 36px 18px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 0;
}
.about-card__top {
  display: flex;
  gap: 24px;
  align-items: flex-start;
  flex: none;
}
.about-card__photo {
  width: 165px;
  height: 200px;
  border-radius: 16px;
  object-fit: cover;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
  flex: none;
}
.about-card__info {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 7px;
}
.about-card__meta-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  font-size: 17px;
  line-height: 1.3;
}
.about-card__meta-row b {
  color: var(--text);
  font-weight: 700;
  margin-right: 6px;
}
.about-card__meta-item {
  color: var(--text-2);
}
.about-card__edu {
  font-size: 14.5px;
  line-height: 1.35;
  color: var(--text-2);
}
.about-card__edu b {
  color: var(--text);
  font-weight: 700;
  margin-right: 6px;
}
.about-card__skills-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5px 16px;
  margin-top: 3px;
}
.about-card__skill {
  display: flex;
  align-items: center;
  gap: 7px;
  color: var(--text-2);
  font-size: 13px;
  line-height: 1.35;
  white-space: nowrap;
}
.about-card__skill::before {
  content: "";
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--accent);
  flex: none;
}
.about-card__badges-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 4px;
  padding-top: 8px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}
.about-card__stack-group,
.about-card__connect-group {
  display: flex;
  align-items: center;
  gap: 7px;
}
.about-card__group-label {
  color: var(--text);
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  margin-right: 2px;
}
.about-card__pill {
  display: inline-flex;
  align-items: center;
  padding: 4px 9px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: var(--text);
  font-size: 12px;
  font-weight: 600;
  text-decoration: none;
  transition: transform 0.2s, background 0.2s;
}
.about-card__pill:hover {
  transform: translateY(-2px);
  background: rgba(255, 255, 255, 0.16);
  border-color: var(--accent);
}
.about-card__pill--accent {
  background: rgba(255, 90, 31, 0.15);
  border-color: rgba(255, 90, 31, 0.4);
  color: #ff9166;
}
.about-card__pill--accent:hover {
  background: rgba(255, 90, 31, 0.25);
  color: #fff;
}
.about-card__bio {
  margin: 10px 0 0;
  padding: 10px 14px;
  border-radius: 12px;
  background: rgba(0, 0, 0, 0.25);
  border: 1px solid rgba(255, 255, 255, 0.06);
  color: var(--text-2);
  font-size: 13.5px;
  line-height: 1.5;
  flex: none;
}
.about-card__cta {
  display: flex;
  justify-content: center;
  margin-top: 10px;
  flex: none;
}
.about-card__cta .linkish {
  font-size: 18px;
  gap: 10px;
}
"""

if "PERFECT ABOUT CARD LAYOUT" not in css:
    css += "\n" + about_card_css
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css)
    print("style.css updated with .about-card flex layout!")
else:
    # Update existing block
    css = re.sub(r"/\* =+ PERFECT ABOUT CARD LAYOUT.*?\.about-card__cta \.linkish\s*\{[^}]*\}", about_card_css.strip(), css, flags=re.DOTALL)
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css)
    print("style.css re-saved with refined .about-card flex layout!")

# =========================================================================
# 2. UPDATE HTML: REPLACE FACE ABOUT WITH CLEAN ABOUT-CARD MARKUP
# =========================================================================
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

new_about_face = """            <!-- Front Side: About Me Profile Card -->
            <article class="face about about-card">
              <h2 class="about-card__head">Software Developer &amp; AI Engineer</h2>
              
              <div class="about-card__body">
                <div class="about-card__top">
                  <img class="about-card__photo" src="https://avatars.githubusercontent.com/u/262732549?v=4" alt="Muffaser Naeem's profile avatar">
                  
                  <div class="about-card__info">
                    <div class="about-card__meta-row">
                      <span class="about-card__meta-item"><b>Name:</b> Muffaser Naeem</span>
                      <span class="about-card__meta-item"><b>Location:</b> Lahore, Pakistan</span>
                    </div>

                    <div class="about-card__edu">
                      <b>Education:</b> COMSATS University Islamabad &middot; BS CS (Batch 29)
                    </div>

                    <div class="about-card__skills-grid">
                      <span class="about-card__skill">Full-Stack Software Developer</span>
                      <span class="about-card__skill">Client-Side WASM &amp; Media Systems</span>
                      <span class="about-card__skill">Applied AI &amp; Deep Learning Builder</span>
                      <span class="about-card__skill">RESTful Microservices &amp; API Design</span>
                      <span class="about-card__skill">Hackathon Winner &amp; Open Source</span>
                      <span class="about-card__skill">Algorithmic Problem-Solving (C++ / Python)</span>
                    </div>

                    <div class="about-card__badges-row">
                      <div class="about-card__stack-group">
                        <span class="about-card__group-label">Core Stack:</span>
                        <span class="about-card__pill">TypeScript</span>
                        <span class="about-card__pill">Python</span>
                        <span class="about-card__pill">JavaScript</span>
                        <span class="about-card__pill">PyTorch</span>
                        <span class="about-card__pill">C++</span>
                      </div>
                      <div class="about-card__connect-group">
                        <span class="about-card__group-label">Connect:</span>
                        <a class="about-card__pill about-card__pill--accent" href="https://github.com/muffasernaeem302" target="_blank" rel="noopener">GitHub ↗</a>
                        <a class="about-card__pill about-card__pill--accent" href="https://www.linkedin.com/in/muffaser-naeem-943475382/" target="_blank" rel="noopener">LinkedIn ↗</a>
                      </div>
                    </div>
                  </div>
                </div>

                <p class="about-card__bio">
                  Software Developer and AI Engineer pursuing a BS in Computer Science at COMSATS University Islamabad. Driven by a builder mindset, I design and engineer scalable web applications, applied AI systems, and high-performance developer utilities. Recent work includes civic intelligence platforms with automated computer vision triage (FixMyCity), clinical conversational AI agents (DentalAI), from-scratch deep learning transformer models (Mini-GPT), and privacy-preserving client-side media engines (OMNI Compression). Focused on clean, maintainable code that solves real-world challenges.
                </p>

                <div class="about-card__cta">
                  <button class="linkish" data-flip="exp">
                    <span>View Education, Technical Experience &amp; Full Skills</span>
                    <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10h14M11 4l6 6-6 6"></path></svg>
                  </button>
                </div>
              </div>
            </article>"""

pattern_face_about = r"<!-- Front Side: About Me Profile Card -->\s*<article class=\"face about.*?</article>"
if not re.search(pattern_face_about, html, flags=re.DOTALL):
    # Fallback pattern
    pattern_face_about = r"<article class=\"face about.*?</article>"

html, count = re.subn(pattern_face_about, new_about_face, html, count=1, flags=re.DOTALL)
print(f"Face about replaced in HTML: {count}")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Replacement complete and saved to index.html!")
