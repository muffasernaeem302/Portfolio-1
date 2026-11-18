# -*- coding: utf-8 -*-
import re

html_path = r"C:\Users\Pc\Downloads\minhngo-space\minhngo-space\index.html"
css_path = r"C:\Users\Pc\Downloads\minhngo-space\minhngo-space\minhngo-space\style.css"

# =========================================================================
# 1. UPDATE STYLE.CSS FOR VAULT MODAL
# =========================================================================
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

vault_css = """
/* ---------- GitHub Vault Modal Styles ---------- */
.vault-close {
  left: 1316px;
  top: 128px;
  z-index: 3;
}
.is-portrait .vault-close {
  left: auto;
  top: max(14px, env(safe-area-inset-top));
}
.vault-hero {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 20px;
  gap: 20px;
}
.vault-hero h2 {
  margin: 0;
  font-size: 34px;
  line-height: 42px;
  letter-spacing: -0.5px;
}
.vault-hero__btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 18px;
  border-radius: 12px;
  background: #20232a;
  color: #fff;
  font-size: 13.5px;
  font-weight: 700;
  text-decoration: none;
  white-space: nowrap;
  transition: transform 0.25s, background 0.25s;
  flex: none;
}
.vault-hero__btn:hover {
  background: var(--accent);
  color: #0d0e11;
  transform: translateY(-2px);
}
"""

if "GitHub Vault Modal Styles" not in css:
    css += "\n" + vault_css
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css)
    print("style.css updated with Vault modal styles")

# =========================================================================
# 2. UPDATE INDEX.HTML FOR VAULT MODAL
# =========================================================================
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# A. Update navbar dropdown
dropdown_old = """        <div class="dropdown" role="menu">
          <button role="menuitem" data-open="projects">Featured GitHub Projects</button>
          <button role="menuitem" data-open="apps">AI &amp; Machine Learning</button>
          <button role="menuitem" data-open="camera">Content Creator Projects</button>
          <button role="menuitem" data-open="brand">Web &amp; Developer Tools</button>
        </div>"""

dropdown_new = """        <div class="dropdown" role="menu">
          <button role="menuitem" data-open="projects">Featured Projects (Interactive Showcase)</button>
          <button role="menuitem" data-open="vault">GitHub Repository Vault (All Repos)</button>
          <button role="menuitem" data-open="apps">AI &amp; Machine Learning</button>
          <button role="menuitem" data-open="brand">Web &amp; Developer Tools</button>
          <button role="menuitem" data-open="camera">Content Creator Projects</button>
        </div>"""

if dropdown_old in html:
    html = html.replace(dropdown_old, dropdown_new)
    print("Dropdown updated in navbar!")

# B. Update box folder element: change data-key="projects" to data-key="vault" and label to GitHub Vault
folder_old = """      <div class="layer obj obj--folder" data-key="projects" style="--i:2; --tilt:3deg">
        <div class="art"><img src="minhngo-space/assets/box/folder.png" alt=""><img class="obj__hover" src="minhngo-space/assets/box/folder-hover.png" alt=""><div class="hit" role="button" tabindex="-1" aria-label="Featured GitHub projects"></div></div>
        <p class="obj__label" aria-hidden="true">GitHub<br>projects</p>
      </div>"""

folder_new = """      <div class="layer obj obj--folder" data-key="vault" style="--i:2; --tilt:3deg">
        <div class="art"><img src="minhngo-space/assets/box/folder.png" alt=""><img class="obj__hover" src="minhngo-space/assets/box/folder-hover.png" alt=""><div class="hit" role="button" tabindex="-1" aria-label="GitHub Open Source Vault"></div></div>
        <p class="obj__label" aria-hidden="true">GitHub<br>Vault</p>
      </div>"""

if folder_old in html:
    html = html.replace(folder_old, folder_new)
    print("Folder object updated to data-key='vault'!")

# C. Update Swatch aria-label and label for clarity
swatch_old = """      <div class="layer obj obj--swatch" data-key="projects" style="--i:3; --tilt:5deg">
        <div class="art"><img src="minhngo-space/assets/box/swatch.png" alt=""><img class="obj__hover" src="minhngo-space/assets/box/swatch-hover.png" alt=""><div class="hit" role="button" tabindex="-1" aria-label="Featured GitHub projects"></div></div>
        <p class="obj__label" aria-hidden="true">Featured<br>projects</p>
      </div>"""

swatch_new = """      <div class="layer obj obj--swatch" data-key="projects" style="--i:3; --tilt:5deg">
        <div class="art"><img src="minhngo-space/assets/box/swatch.png" alt=""><img class="obj__hover" src="minhngo-space/assets/box/swatch-hover.png" alt=""><div class="hit" role="button" tabindex="-1" aria-label="Featured Projects Interactive Showcase"></div></div>
        <p class="obj__label" aria-hidden="true">Featured<br>projects</p>
      </div>"""

if swatch_old in html:
    html = html.replace(swatch_old, swatch_new)
    print("Swatch object updated!")

# D. Insert the new GitHub Vault modal right after projects modal
vault_modal_html = """
      <!-- GitHub Open-Source Repository Vault -->
      <section class="modal" data-modal="vault" aria-label="GitHub Open-Source Repository Vault">
        <div class="pop github-projects">
          <div class="vault-hero">
            <div>
              <h2>GitHub Repository Vault</h2>
              <p class="github-projects__intro" style="margin-bottom:0;">A complete directory of all public open-source repositories, developer tools, AI research experiments, and contributions authored by Muffaser Naeem.</p>
            </div>
            <a class="vault-hero__btn" href="https://github.com/muffasernaeem302?tab=repositories" target="_blank" rel="noopener">
              <span>View Profile on GitHub</span>
              <span aria-hidden="true">↗</span>
            </a>
          </div>

          <div class="github-project-grid">

            <!-- 1. FixMyCity -->
            <a class="github-project" href="https://github.com/muffasernaeem302/FIX-MY-CITY-PROJECT-HACKATHON" target="_blank" rel="noopener">
              <span class="github-project__type">Civic AI Platform &middot; Hackathon Project</span>
              <h3>FIX-MY-CITY-PROJECT-HACKATHON</h3>
              <div class="github-project-tags">
                <span class="github-project-tag">Python</span>
                <span class="github-project-tag">FastAPI</span>
                <span class="github-project-tag">Computer Vision</span>
                <span class="github-project-tag">JavaScript</span>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">Repository Overview</span>
                <p>AI-assisted municipal infrastructure reporting platform. Analyzes citizen photos, estimates urgency scores, clusters duplicate reports, and automatically dispatches tasks to city departments.</p>
              </div>
              <span class="github-project__link"><span>View on GitHub</span> <span>↗</span></span>
            </a>

            <!-- 2. DentalAI Bot -->
            <a class="github-project" href="https://github.com/muffasernaeem302/DENTAL-AI-BOT-" target="_blank" rel="noopener">
              <span class="github-project__type">Healthcare AI &middot; Conversational Bot</span>
              <h3>DENTAL-AI-BOT-</h3>
              <div class="github-project-tags">
                <span class="github-project-tag">TypeScript</span>
                <span class="github-project-tag">Python</span>
                <span class="github-project-tag">NLP / LLMs</span>
                <span class="github-project-tag">Medical Guardrails</span>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">Repository Overview</span>
                <p>Specialized clinical triage assistant providing conversational oral health guidance, symptom evaluation, patient education, and red-flag emergency escalation protocols.</p>
              </div>
              <span class="github-project__link"><span>View on GitHub</span> <span>↗</span></span>
            </a>

            <!-- 3. Mini-GPT -->
            <a class="github-project" href="https://github.com/muffasernaeem302/Mini_-GPT" target="_blank" rel="noopener">
              <span class="github-project__type">Generative AI &middot; Deep Learning</span>
              <h3>Mini_-GPT</h3>
              <div class="github-project-tags">
                <span class="github-project-tag">Python</span>
                <span class="github-project-tag">PyTorch</span>
                <span class="github-project-tag">Causal Self-Attention</span>
                <span class="github-project-tag">CUDA</span>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">Repository Overview</span>
                <p>From-scratch PyTorch implementation of an autoregressive Generative Pre-trained Transformer language model. Explores multi-head attention, layer normalization, tokenization, and temperature sampling.</p>
              </div>
              <span class="github-project__link"><span>View on GitHub</span> <span>↗</span></span>
            </a>

            <!-- 4. Git Pulse Finder -->
            <a class="github-project" href="https://github.com/muffasernaeem302/Git-Pulse-Finder-Website" target="_blank" rel="noopener">
              <span class="github-project__type">Developer Tool &middot; Ecosystem Analytics</span>
              <h3>Git-Pulse-Finder-Website</h3>
              <div class="github-project-tags">
                <span class="github-project-tag">JavaScript (ES2024)</span>
                <span class="github-project-tag">GitHub REST API</span>
                <span class="github-project-tag">Client Caching</span>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">Repository Overview</span>
                <p>Real-time GitHub profile explorer and developer scorecard. Queries repositories, commit frequencies, and language distributions with client-side caching to prevent rate-limit bottlenecks.</p>
              </div>
              <span class="github-project__link"><span>View on GitHub</span> <span>↗</span></span>
            </a>

            <!-- 5. OMNI Compression -->
            <a class="github-project" href="https://github.com/muffasernaeem302/OMNI-COMPRESSION-" target="_blank" rel="noopener">
              <span class="github-project__type">Media Engine &middot; WebAssembly</span>
              <h3>OMNI-COMPRESSION-</h3>
              <div class="github-project-tags">
                <span class="github-project-tag">TypeScript</span>
                <span class="github-project-tag">WebAssembly</span>
                <span class="github-project-tag">Canvas 2D</span>
                <span class="github-project-tag">Web Workers</span>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">Repository Overview</span>
                <p>Client-side image and video compression utility achieving 60–85% file size reduction with zero server uploads, leveraging Canvas 2D and multithreaded WASM workers.</p>
              </div>
              <span class="github-project__link"><span>View on GitHub</span> <span>↗</span></span>
            </a>

            <!-- 6. TypeFlow -->
            <a class="github-project" href="https://github.com/muffasernaeem302/Type_Flow-Project-" target="_blank" rel="noopener">
              <span class="github-project__type">Productivity &middot; Offline App</span>
              <h3>Type_Flow-Project-</h3>
              <div class="github-project-tags">
                <span class="github-project-tag">TypeScript</span>
                <span class="github-project-tag">Performance API</span>
                <span class="github-project-tag">IndexedDB</span>
                <span class="github-project-tag">Offline-First</span>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">Repository Overview</span>
                <p>Zero-latency offline typing speed and accuracy trainer with microsecond-level keystroke telemetry, error heatmaps, and LocalStorage progression tracking.</p>
              </div>
              <span class="github-project__link"><span>View on GitHub</span> <span>↗</span></span>
            </a>

            <!-- 7. VibeSync -->
            <a class="github-project" href="https://github.com/muffasernaeem302/Vibe_Sync" target="_blank" rel="noopener">
              <span class="github-project__type">Music Intelligence &middot; Spotify API</span>
              <h3>Vibe_Sync</h3>
              <div class="github-project-tags">
                <span class="github-project-tag">TypeScript</span>
                <span class="github-project-tag">Spotify API</span>
                <span class="github-project-tag">OAuth 2.0 PKCE</span>
                <span class="github-project-tag">Vector Clustering</span>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">Repository Overview</span>
                <p>Algorithmic playlist curation tool interfacing with the Spotify Web API. Computes acoustic distance matrices across song attributes to cluster tracks into harmonious mood playlists.</p>
              </div>
              <span class="github-project__link"><span>View on GitHub</span> <span>↗</span></span>
            </a>

          </div>
        </div>
        <button class="pop close vault-close" data-close="" style="--d:2" aria-label="Close">
          <svg viewBox="0 0 42 42" fill="none" stroke="currentColor" stroke-width="5.5" stroke-linecap="round"><path d="M4 4l34 34M38 4L4 38"></path></svg>
        </button>
      </section>
"""

# Insert vault_modal_html right after projects modal closing </section>
pattern_proj_end = r'(<section class="modal" data-modal="projects".*?</section>)'
match = re.search(pattern_proj_end, html, flags=re.DOTALL)
if match and "data-modal=\"vault\"" not in html:
    html = html[:match.end()] + "\n" + vault_modal_html + html[match.end():]
    print("Vault modal inserted into HTML!")

# E. Update MODALS array in JavaScript
js_modals_old = "const MODALS = ['about', 'apps', 'projects', 'brand', 'camera'];"
js_modals_new = "const MODALS = ['about', 'apps', 'projects', 'vault', 'brand', 'camera'];"

if js_modals_old in html:
    html = html.replace(js_modals_old, js_modals_new)
    print("MODALS array updated with 'vault'!")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("All changes successfully applied to index.html!")
