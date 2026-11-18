# -*- coding: utf-8 -*-
import re

html_path = r"C:\Users\Pc\Downloads\minhngo-space\minhngo-space\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# ---------------------------------------------------------------------------
# 1. NEW AI & MACHINE LEARNING MODAL (APPS)
# ---------------------------------------------------------------------------
new_apps_modal = """      <!-- AI and machine learning projects -->
      <section class="modal" data-modal="apps" aria-label="AI and machine learning projects">
        <div class="pop github-projects">
          <h2>AI &amp; Machine Learning</h2>
          <p class="github-projects__intro">Production-grade AI applications and deep learning research &mdash; built from foundational principles to solve genuine healthcare, civic, and natural language challenges.</p>
          <div class="github-project-grid">

            <!-- FixMyCity -->
            <a class="github-project" href="https://github.com/muffasernaeem302/FIX-MY-CITY-PROJECT-HACKATHON" target="_blank" rel="noopener">
              <span class="github-project__type">Civic AI Platform &middot; Hackathon Project</span>
              <h3>FixMyCity</h3>
              <div class="github-project-tags">
                <span class="github-project-tag">Python</span>
                <span class="github-project-tag">FastAPI</span>
                <span class="github-project-tag">Computer Vision</span>
                <span class="github-project-tag">JavaScript</span>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">What It Does</span>
                <p>Empowers citizens to report urban infrastructure issues (potholes, burst pipelines, broken lighting, sanitation hazards) via quick photo upload. Eliminates municipal paperwork by automating triage and dispatch.</p>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">How I Made It &amp; Architecture</span>
                <p>Engineered a FastAPI Python backend coupled with a computer vision pipeline for automated image classification and urgency estimation. Built geospatial coordinate clustering combined with image hashing to automatically merge duplicate citizen reports, routing prioritized work orders directly to municipal department queues.</p>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">Key Engineering Highlights</span>
                <ul>
                  <li>Reduces duplicate reports by ~70% using geo-clustering and visual hashing</li>
                  <li>Instant issue categorization with automated ward boundary dispatch</li>
                </ul>
              </div>
              <span class="github-project__link">View repository on GitHub <span>↗</span></span>
            </a>

            <!-- DentalAI -->
            <a class="github-project" href="https://github.com/muffasernaeem302/DENTAL-AI-BOT-" target="_blank" rel="noopener">
              <span class="github-project__type">Clinical AI Assistant &middot; Full-Stack</span>
              <h3>DentalAI Bot</h3>
              <div class="github-project-tags">
                <span class="github-project-tag">TypeScript</span>
                <span class="github-project-tag">Python</span>
                <span class="github-project-tag">NLP / LLMs</span>
                <span class="github-project-tag">Clinical Triage</span>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">What It Does</span>
                <p>An intelligent oral-health conversational assistant providing immediate, clinically-grounded guidance, symptom evaluation, patient education, and urgent referral warnings for dental patients.</p>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">How I Made It &amp; Architecture</span>
                <p>Designed a TypeScript conversational frontend integrated with a Python NLP backend querying structured dental knowledge bases. Implemented multi-turn dialogue memory and rigorous triage guardrails to detect high-risk symptoms (facial swelling, acute trauma) and prioritize emergency protocols over general advice.</p>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">Key Engineering Highlights</span>
                <ul>
                  <li>Strict clinical guardrails preventing unqualified medical prescriptions</li>
                  <li>Real-time response streaming with symptom pill suggestions</li>
                </ul>
              </div>
              <span class="github-project__link">View repository on GitHub <span>↗</span></span>
            </a>

            <!-- Mini-GPT -->
            <a class="github-project" href="https://github.com/muffasernaeem302/Mini_-GPT" target="_blank" rel="noopener">
              <span class="github-project__type">Generative AI &middot; Transformer Research</span>
              <h3>Mini-GPT</h3>
              <div class="github-project-tags">
                <span class="github-project-tag">Python</span>
                <span class="github-project-tag">PyTorch</span>
                <span class="github-project-tag">Causal Attention</span>
                <span class="github-project-tag">CUDA</span>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">What It Does</span>
                <p>A from-scratch deep learning implementation of a Generative Pre-trained Transformer (GPT) language model, built without third-party LLM frameworks to investigate and master transformer mechanics.</p>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">How I Made It &amp; Architecture</span>
                <p>Constructed decoder-only transformer blocks in PyTorch: multi-head causal self-attention, learnable positional and token embeddings, layer normalization, residual skip-connections, and GELU feed-forward networks. Built custom tokenization, AdamW training with cosine learning rate schedules, and autoregressive generation with temperature and top-k sampling.</p>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">Key Engineering Highlights</span>
                <ul>
                  <li>100% written in PyTorch from mathematical fundamentals</li>
                  <li>Autoregressive sampling with temperature &amp; top-k controls</li>
                </ul>
              </div>
              <span class="github-project__link">View repository on GitHub <span>↗</span></span>
            </a>

          </div>
        </div>
        <button class="pop close apps-close" data-close="" style="--d:2" aria-label="Close">
          <svg viewBox="0 0 42 42" fill="none" stroke="currentColor" stroke-width="5.5" stroke-linecap="round"><path d="M4 4l34 34M38 4L4 38"></path></svg>
        </button>
      </section>"""

# ---------------------------------------------------------------------------
# 2. NEW FEATURED PROJECTS MODAL (PHONE SHOWCASE WITH 6 DETAILED APPS)
# ---------------------------------------------------------------------------
new_projects_modal = """      <!-- Featured GitHub projects -->
      <section class="modal" data-modal="projects" aria-label="Featured GitHub projects">
        <div class="pop project-showcase">
          <div class="project-showcase__device" aria-label="Choose a project">
            <div class="project-showcase__screen">
              <span class="project-showcase__island" aria-hidden="true"></span>
              <p class="project-showcase__device-label">MUFFASER <span>&middot;</span> PROJECTS</p>
              <div class="project-showcase__grid" role="group" aria-label="Featured projects">
                
                <button class="project-showcase__app is-selected" type="button" aria-pressed="true" 
                  data-title="FixMyCity" 
                  data-kind="Civic AI &middot; Hackathon" 
                  data-subtitle="Automated civic issue reporting, computer-vision triage &amp; municipal dispatch" 
                  data-does="A civic intelligence web platform that empowers citizens to report urban infrastructure failures (potholes, water leaks, broken street lighting, hazardous waste) directly to municipal authorities by uploading a single photo and brief note. The system eliminates bureaucratic latency and duplicate reports." 
                  data-how="Built a FastAPI Python backend coupled with a computer vision pipeline for automated image classification and urgency estimation. Built geospatial coordinate clustering combined with image hashing to automatically merge duplicate citizen reports, routing prioritized work orders directly to municipal department queues." 
                  data-highlights="Reduces duplicate citizen filings by ~70% via geo-radius and visual similarity clustering|Automated ticket dispatch mapping detected issues directly to municipal department queues|Responsive mobile-first submission interface with geolocation capture" 
                  data-stack="JavaScript &middot; Python &middot; FastAPI &middot; Computer Vision &middot; Geolocation API" 
                  data-role="Lead Full-Stack &amp; AI Architect" 
                  data-repo="https://github.com/muffasernaeem302/FIX-MY-CITY-PROJECT-HACKATHON">
                  <span class="project-showcase__icon project-showcase__icon--city" aria-hidden="true">FC</span>
                  <span class="project-showcase__app-name">FixMyCity</span>
                </button>

                <button class="project-showcase__app" type="button" aria-pressed="false" 
                  data-title="DentalAI Bot" 
                  data-kind="Clinical AI Assistant" 
                  data-subtitle="Intelligent oral-health conversational assistant with safety guardrails" 
                  data-does="A specialized AI conversational assistant designed to bridge the gap between dental symptoms and patient understanding. It provides immediate, clinically grounded oral-health guidance, symptom assessment, hygiene recommendations, and dental terminology clarification." 
                  data-how="Built an asynchronous conversational engine in TypeScript with a Python backend that parses natural language queries, classifies user concerns, and matches them with vetted dental knowledge bases. Engineered strict triage heuristics and system prompt guardrails to identify red-flag dental emergencies (e.g. facial swelling, severe trauma) and prioritize clinical referrals." 
                  data-highlights="Engineered safety guardrails preventing unqualified medical prescriptions while delivering accurate health literacy|Multi-turn context retention for evaluating evolving symptom timelines|Interactive chat interface with quick-reply symptom suggestion pills" 
                  data-stack="TypeScript &middot; Python &middot; NLP / LLMs &middot; REST APIs &middot; Clinical Triage" 
                  data-role="Full-Stack &amp; AI Prompt Engineer" 
                  data-repo="https://github.com/muffasernaeem302/DENTAL-AI-BOT-">
                  <span class="project-showcase__icon project-showcase__icon--dental" aria-hidden="true">D</span>
                  <span class="project-showcase__app-name">DentalAI</span>
                </button>

                <button class="project-showcase__app" type="button" aria-pressed="false" 
                  data-title="Git Pulse Finder" 
                  data-kind="Developer Intelligence Tool" 
                  data-subtitle="Instant GitHub ecosystem analytics, developer metrics &amp; repo visualizer" 
                  data-does="A developer productivity web application that provides real-time analytics, repository breakdowns, language distributions, and commit insights for any GitHub profile or organization without requiring manual page navigation." 
                  data-how="Integrated the GitHub REST v3 API with optimized asynchronous requests (Promise.all), implementing client-side request caching and rate-limit tracking to deliver instant search experiences. Implemented client-side statistical aggregations calculating language percentages, repository popularity metrics, and activity timelines without server overhead." 
                  data-highlights="Zero external frameworks &mdash; 100% vanilla modern JavaScript for maximum performance and sub-100ms response times|Instant client-side multi-filter across repositories by language, stars, and recency|Client-side caching layer minimizing redundant GitHub API calls" 
                  data-stack="JavaScript (ES2024) &middot; GitHub REST API v3 &middot; CSS3 Grid/Flexbox &middot; Async/Await" 
                  data-role="Frontend &amp; API Integration Developer" 
                  data-repo="https://github.com/muffasernaeem302/Git-Pulse-Finder-Website">
                  <span class="project-showcase__icon project-showcase__icon--pulse" aria-hidden="true">&lt;/&gt;</span>
                  <span class="project-showcase__app-name">Git Pulse</span>
                </button>

                <button class="project-showcase__app" type="button" aria-pressed="false" 
                  data-title="OMNI Compression" 
                  data-kind="Media Optimization Engine" 
                  data-subtitle="Browser-native image &amp; video compression with client-side WebAssembly" 
                  data-does="A modern client-side media compression and format conversion utility. It enables developers, content creators, and everyday users to drastically reduce image and video file sizes (often 60–85% reduction) right in their browser without uploading sensitive media to remote third-party servers." 
                  data-how="Built with TypeScript leveraging HTML5 Canvas 2D API for high-performance pixel manipulation, bicubic scaling, and quality-controlled JPEG/WebP encoding. Integrated WebAssembly multimedia compilation for multithreaded client-side video frame transcoding and bitrate adjustment without server dependencies, managing memory via URL.revokeObjectURL()." 
                  data-highlights="100% client-side execution guaranteeing complete privacy &mdash; media never leaves the user's browser|Multithreaded Web Worker architecture keeping the main UI thread completely fluid at 60fps|Real-time split-screen visual diff slider allowing users to inspect compression fidelity before saving" 
                  data-stack="TypeScript &middot; HTML5 Canvas API &middot; WebAssembly (WASM) &middot; Web Workers &middot; FileSystem API" 
                  data-role="Systems &amp; Media Processing Developer" 
                  data-repo="https://github.com/muffasernaeem302/OMNI-COMPRESSION-">
                  <span class="project-showcase__icon project-showcase__icon--omni" aria-hidden="true">O</span>
                  <span class="project-showcase__app-name">OMNI</span>
                </button>

                <button class="project-showcase__app" type="button" aria-pressed="false" 
                  data-title="VibeSync" 
                  data-kind="Music Intelligence &middot; Productivity" 
                  data-subtitle="Spotify library acoustic feature analysis &amp; automated mood clustering" 
                  data-does="An intelligent music curation tool that interfaces with Spotify to analyze the mathematical audio characteristics of user libraries and automatically curates harmonious playlists grouped by mood, tempo, energy, and acoustic properties." 
                  data-how="Implemented OAuth 2.0 with Proof Key for Code Exchange (PKCE) for secure token-based authorization entirely within the client. Queried Spotify's audio analysis endpoints to extract multi-dimensional metrics (valence, energy, danceability, acousticness, tempo) and developed heuristic clustering algorithms to group complementary tracks into distinct mood buckets with one-click batch sync." 
                  data-highlights="Implemented secure client-side OAuth 2.0 PKCE authentication requiring zero server secrets|Multidimensional acoustic distance clustering across valence, energy, and tempo matrices|One-click batch playlist synchronization with automatic duplicate track prevention" 
                  data-stack="TypeScript &middot; Spotify Web API &middot; OAuth 2.0 PKCE &middot; Vector Clustering &middot; Asynchronous Architecture" 
                  data-role="Lead Full-Stack Developer" 
                  data-repo="https://github.com/muffasernaeem302/Vibe_Sync">
                  <span class="project-showcase__icon project-showcase__icon--vibe" aria-hidden="true">V</span>
                  <span class="project-showcase__app-name">VibeSync</span>
                </button>

                <button class="project-showcase__app" type="button" aria-pressed="false" 
                  data-title="Mini-GPT" 
                  data-kind="Generative AI &middot; Transformer Architecture" 
                  data-subtitle="From-scratch autoregressive language model implementation in PyTorch" 
                  data-does="An authentic, from-scratch deep learning implementation of a Generative Pre-trained Transformer (GPT) language model. Built to demonstrate and study the foundational mechanics of generative AI, attention mechanisms, and autoregressive text generation." 
                  data-how="Implemented decoder-only transformer blocks in PyTorch without high-level abstractions: multi-head causal self-attention, scaled dot-product attention matrices, learnable token and positional embedding tables, and layer normalization layers. Trained on custom story datasets with cross-entropy loss and AdamW optimizer with cosine learning rate scheduling." 
                  data-highlights="100% written in PyTorch from mathematical fundamentals &mdash; no third-party transformer wrappers|Autoregressive text generation with customizable temperature scaling and top-k sampling|CUDA acceleration support for high-throughput GPU training and generation" 
                  data-stack="Python &middot; PyTorch &middot; Causal Self-Attention &middot; CUDA GPU &middot; Tokenization" 
                  data-role="Deep Learning Researcher &amp; Author" 
                  data-repo="https://github.com/muffasernaeem302/Mini_-GPT">
                  <span class="project-showcase__icon project-showcase__icon--gpt" aria-hidden="true">GPT</span>
                  <span class="project-showcase__app-name">Mini-GPT</span>
                </button>

              </div>
              <p class="project-showcase__device-hint">Tap any icon on the device to inspect the project</p>
            </div>
          </div>

          <!-- Project Detail Showcase Card -->
          <article class="project-showcase__details" aria-live="polite">
            <p class="project-showcase__eyebrow">FEATURED GITHUB PROJECT <span aria-hidden="true">&middot;</span> <span id="showcaseKind">Civic AI &middot; Hackathon</span></p>
            <h2 id="showcaseTitle">FixMyCity</h2>
            <p class="project-showcase__subtitle" id="showcaseSubtitle">Automated civic issue reporting, computer-vision triage &amp; municipal dispatch</p>
            
            <div class="project-showcase__section">
              <h3 class="project-showcase__section-title">What It Does</h3>
              <p class="project-showcase__section-text" id="showcaseDoes">A civic intelligence web platform that empowers citizens to report urban infrastructure failures (potholes, water leaks, broken street lighting, hazardous waste) directly to municipal authorities by uploading a single photo and brief note. The system eliminates bureaucratic latency and duplicate reports.</p>
            </div>

            <div class="project-showcase__section">
              <h3 class="project-showcase__section-title">How I Made It &amp; Architecture</h3>
              <p class="project-showcase__section-text" id="showcaseHow">Built a FastAPI Python backend coupled with a computer vision pipeline for automated image classification and urgency estimation. Built geospatial coordinate clustering combined with image hashing to automatically merge duplicate citizen reports, routing prioritized work orders directly to municipal department queues.</p>
            </div>

            <div class="project-showcase__section">
              <h3 class="project-showcase__section-title">Key Engineering Highlights</h3>
              <ul class="project-showcase__highlights" id="showcaseHighlights">
                <li>Reduces duplicate citizen filings by ~70% via geo-radius and visual similarity clustering</li>
                <li>Automated ticket dispatch mapping detected issues directly to municipal department queues</li>
                <li>Responsive mobile-first submission interface with geolocation capture</li>
              </ul>
            </div>

            <dl class="project-showcase__facts">
              <div><dt>Category:</dt><dd id="showcaseCategory">Civic AI &middot; Hackathon</dd></div>
              <div><dt>Technologies:</dt><dd id="showcaseStack">JavaScript &middot; Python &middot; FastAPI &middot; Computer Vision &middot; Geolocation API</dd></div>
              <div><dt>Engineering Focus:</dt><dd id="showcaseRole">Lead Full-Stack &amp; AI Architect</dd></div>
              <div><dt>Platform:</dt><dd>GitHub Open Source</dd></div>
            </dl>
            <a class="project-showcase__repo" id="showcaseRepo" href="https://github.com/muffasernaeem302/FIX-MY-CITY-PROJECT-HACKATHON" target="_blank" rel="noopener">View project on GitHub <span aria-hidden="true">↗</span></a>
            <a class="project-showcase__all" href="https://github.com/muffasernaeem302?tab=repositories" target="_blank" rel="noopener">Browse all repositories on GitHub <span aria-hidden="true">↗</span></a>
          </article>
        </div>
        <button class="pop close projects-close" data-close="" style="--d:3" aria-label="Close">
          <svg viewBox="0 0 42 42" fill="none" stroke="currentColor" stroke-width="5.5" stroke-linecap="round"><path d="M4 4l34 34M38 4L4 38"></path></svg>
        </button>
      </section>"""

# ---------------------------------------------------------------------------
# 3. NEW WEB & DEV TOOLS MODAL (BRAND - 4 DETAILED PROJECTS)
# ---------------------------------------------------------------------------
new_brand_modal = """      <!-- Web and developer tools -->
      <section class="modal" data-modal="brand" aria-label="Web and developer tools">
        <div class="pop github-projects">
          <h2>Web &amp; Developer Tools</h2>
          <p class="github-projects__intro">High-utility web applications, developer platforms, and media utilities &mdash; engineered with modern TypeScript and JavaScript for performance, privacy, and zero latency.</p>
          <div class="github-project-grid">

            <!-- Git Pulse Finder -->
            <a class="github-project" href="https://github.com/muffasernaeem302/Git-Pulse-Finder-Website" target="_blank" rel="noopener">
              <span class="github-project__type">Developer Tool &middot; Web Application</span>
              <h3>Git Pulse Finder</h3>
              <div class="github-project-tags">
                <span class="github-project-tag">JavaScript ES2024</span>
                <span class="github-project-tag">GitHub REST API</span>
                <span class="github-project-tag">CSS3 Grid</span>
                <span class="github-project-tag">Client Caching</span>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">What It Does</span>
                <p>An instant developer discovery and repository analytics dashboard. Search any GitHub profile or organization to immediately view their language distributions, star ratios, commit activity, and top repositories.</p>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">How I Made It &amp; Architecture</span>
                <p>Constructed using pure modern JavaScript with asynchronous Promise.all fetch pipelines querying GitHub REST v3 endpoints. Features client-side in-memory caching to guard against rate limits, instantaneous client-side filtering, and fluid CSS3 Grid layouts.</p>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">Key Engineering Highlights</span>
                <ul>
                  <li>Zero external dependencies &mdash; sub-100ms load times and optimal bundle size</li>
                  <li>Instant multi-criteria filtering across repositories by language, stars, and recency</li>
                </ul>
              </div>
              <span class="github-project__link">View repository on GitHub <span>↗</span></span>
            </a>

            <!-- OMNI Compression -->
            <a class="github-project" href="https://github.com/muffasernaeem302/OMNI-COMPRESSION-" target="_blank" rel="noopener">
              <span class="github-project__type">Media Engine &middot; Client-Side WASM</span>
              <h3>OMNI Compression</h3>
              <div class="github-project-tags">
                <span class="github-project-tag">TypeScript</span>
                <span class="github-project-tag">HTML5 Canvas</span>
                <span class="github-project-tag">WebAssembly</span>
                <span class="github-project-tag">Web Workers</span>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">What It Does</span>
                <p>A client-side media compression tool that reduces image and video file sizes by 60–85% while preserving visual clarity &mdash; keeping user media 100% private by executing entirely in the browser without server uploads.</p>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">How I Made It &amp; Architecture</span>
                <p>Engineered with TypeScript using the Canvas 2D API for bicubic scaling and quantization control. Integrated multithreaded WebAssembly workers for client-side video transcoding, preventing UI freezes, with memory management to prevent browser memory leaks.</p>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">Key Engineering Highlights</span>
                <ul>
                  <li>Complete client-side privacy &mdash; media never leaves the local machine</li>
                  <li>Live split-screen before/after comparison slider and byte savings calculator</li>
                </ul>
              </div>
              <span class="github-project__link">View repository on GitHub <span>↗</span></span>
            </a>

            <!-- TypeFlow -->
            <a class="github-project" href="https://github.com/muffasernaeem302/Type_Flow-Project-" target="_blank" rel="noopener">
              <span class="github-project__type">Productivity &middot; Offline-First Desktop App</span>
              <h3>TypeFlow</h3>
              <div class="github-project-tags">
                <span class="github-project-tag">TypeScript</span>
                <span class="github-project-tag">Performance API</span>
                <span class="github-project-tag">IndexedDB</span>
                <span class="github-project-tag">Event-Driven</span>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">What It Does</span>
                <p>A distraction-free, offline-first typing performance utility designed to build typing velocity, muscle memory, and raw accuracy. Provides instant real-time telemetry including Net WPM, Gross WPM, keystroke latency, and mistake heatmaps.</p>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">How I Made It &amp; Architecture</span>
                <p>Developed an event-driven keystroke listener using the browser's performance.now() API for microsecond-accurate timing between keystrokes. Built tiered word generation algorithms and offline persistence via LocalStorage and IndexedDB to track historical typing progression.</p>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">Key Engineering Highlights</span>
                <ul>
                  <li>Microsecond keystroke interval telemetry capturing typing hesitation patterns</li>
                  <li>100% offline-first architecture with zero network dependencies or tracking</li>
                </ul>
              </div>
              <span class="github-project__link">View repository on GitHub <span>↗</span></span>
            </a>

            <!-- VibeSync -->
            <a class="github-project" href="https://github.com/muffasernaeem302/Vibe_Sync" target="_blank" rel="noopener">
              <span class="github-project__type">Music Tool &middot; Spotify Web API</span>
              <h3>VibeSync</h3>
              <div class="github-project-tags">
                <span class="github-project-tag">TypeScript</span>
                <span class="github-project-tag">Spotify API</span>
                <span class="github-project-tag">OAuth 2.0 PKCE</span>
                <span class="github-project-tag">Vector Clustering</span>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">What It Does</span>
                <p>An intelligent music curation tool that connects to Spotify to extract acoustic features (valence, energy, tempo, danceability) from user tracks and automatically cluster libraries into harmonious, mood-aligned playlists.</p>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">How I Made It &amp; Architecture</span>
                <p>Integrated the Spotify Web API via client-side OAuth 2.0 PKCE. Developed multidimensional distance clustering across acoustic matrices to group complementary songs into distinct mood buckets with one-click batch playlist creation and deduplication.</p>
              </div>
              <div class="github-project-section">
                <span class="github-project-section-title">Key Engineering Highlights</span>
                <ul>
                  <li>Zero-backend OAuth 2.0 PKCE authentication flow maintaining total security</li>
                  <li>Multidimensional audio vector clustering into cohesive mood playlists</li>
                </ul>
              </div>
              <span class="github-project__link">View repository on GitHub <span>↗</span></span>
            </a>

          </div>
        </div>
        <button class="pop close brand-close" data-close="" style="--d:2" aria-label="Close">
          <svg viewBox="0 0 42 42" fill="none" stroke="currentColor" stroke-width="5.5" stroke-linecap="round"><path d="M4 4l34 34M38 4L4 38"></path></svg>
        </button>
      </section>"""

# ---------------------------------------------------------------------------
# 4. REPLACEMENT IN CONTENT
# ---------------------------------------------------------------------------

# Replace apps modal
pattern_apps = r"<!-- AI and machine learning projects -->\s*<section class=\"modal\" data-modal=\"apps\".*?</section>"
content, count_apps = re.subn(pattern_apps, new_apps_modal, content, flags=re.DOTALL)
print(f"Apps modal replaced: {count_apps}")

# Replace projects modal
pattern_projects = r"<!-- Featured GitHub projects -->\s*<section class=\"modal\" data-modal=\"projects\".*?</section>"
content, count_proj = re.subn(pattern_projects, new_projects_modal, content, flags=re.DOTALL)
print(f"Projects modal replaced: {count_proj}")

# Replace brand modal
pattern_brand = r"<!-- Web and developer tools -->\s*<section class=\"modal\" data-modal=\"brand\".*?</section>"
content, count_brand = re.subn(pattern_brand, new_brand_modal, content, flags=re.DOTALL)
print(f"Brand modal replaced: {count_brand}")

# ---------------------------------------------------------------------------
# 5. UPDATE JAVASCRIPT FOR SHOWCASE BUTTONS
# ---------------------------------------------------------------------------
old_js_showcase = """    const showcaseButtons = document.querySelectorAll('.project-showcase__app');
    const showcaseTitle = document.getElementById('showcaseTitle');
    const showcaseKind = document.getElementById('showcaseKind');
    const showcaseDescription = document.getElementById('showcaseDescription');
    const showcaseCategory = document.getElementById('showcaseCategory');
    const showcaseStack = document.getElementById('showcaseStack');
    const showcaseRepo = document.getElementById('showcaseRepo');
    showcaseButtons.forEach((button) => {
      button.addEventListener('click', () => {
        showcaseButtons.forEach((item) => {
          const selected = item === button;
          item.classList.toggle('is-selected', selected);
          item.setAttribute('aria-pressed', String(selected));
        });
        showcaseTitle.textContent = button.dataset.title;
        showcaseKind.textContent = button.dataset.kind;
        showcaseDescription.textContent = button.dataset.description;
        showcaseCategory.textContent = button.dataset.kind;
        showcaseStack.textContent = button.dataset.stack;
        showcaseRepo.href = button.dataset.repo;
        showcaseRepo.setAttribute('aria-label', `View ${button.dataset.title} project on GitHub`);
      });
    });"""

new_js_showcase = """    const showcaseButtons = document.querySelectorAll('.project-showcase__app');
    const showcaseTitle = document.getElementById('showcaseTitle');
    const showcaseKind = document.getElementById('showcaseKind');
    const showcaseSubtitle = document.getElementById('showcaseSubtitle');
    const showcaseDoes = document.getElementById('showcaseDoes');
    const showcaseHow = document.getElementById('showcaseHow');
    const showcaseHighlights = document.getElementById('showcaseHighlights');
    const showcaseCategory = document.getElementById('showcaseCategory');
    const showcaseStack = document.getElementById('showcaseStack');
    const showcaseRole = document.getElementById('showcaseRole');
    const showcaseRepo = document.getElementById('showcaseRepo');

    showcaseButtons.forEach((button) => {
      button.addEventListener('click', () => {
        showcaseButtons.forEach((item) => {
          const selected = item === button;
          item.classList.toggle('is-selected', selected);
          item.setAttribute('aria-pressed', String(selected));
        });
        if (showcaseTitle) showcaseTitle.textContent = button.dataset.title;
        if (showcaseKind) showcaseKind.textContent = button.dataset.kind;
        if (showcaseSubtitle) showcaseSubtitle.textContent = button.dataset.subtitle || '';
        if (showcaseDoes) showcaseDoes.textContent = button.dataset.does || '';
        if (showcaseHow) showcaseHow.textContent = button.dataset.how || '';
        if (showcaseHighlights) {
          const rawHighlights = button.dataset.highlights || '';
          const items = rawHighlights.split('|').filter(s => s.trim().length > 0);
          showcaseHighlights.innerHTML = items.map(it => `<li>${it.trim()}</li>`).join('');
        }
        if (showcaseCategory) showcaseCategory.textContent = button.dataset.kind;
        if (showcaseStack) showcaseStack.textContent = button.dataset.stack;
        if (showcaseRole) showcaseRole.textContent = button.dataset.role || 'Lead Architecture & Engineering';
        if (showcaseRepo) {
          showcaseRepo.href = button.dataset.repo;
          showcaseRepo.setAttribute('aria-label', `View ${button.dataset.title} project on GitHub`);
        }
      });
    });"""

if old_js_showcase in content:
    content = content.replace(old_js_showcase, new_js_showcase)
    print("Showcase JS replaced successfully!")
else:
    # Try regex fallback for JS
    pattern_js = r"const showcaseButtons = document\.querySelectorAll\('\.project-showcase__app'\);.*?showcaseRepo\.setAttribute\(`View \$\{button\.dataset\.title\} project on GitHub`\);\s*\}\);\s*\}\);"
    content, count_js = re.subn(pattern_js, new_js_showcase, content, flags=re.DOTALL)
    print(f"Showcase JS replaced via regex: {count_js}")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("index.html fully updated with all elaborated projects!")
