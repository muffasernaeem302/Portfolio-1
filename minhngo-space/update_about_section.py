# -*- coding: utf-8 -*-
import re

html_path = r"C:\Users\Pc\Downloads\minhngo-space\minhngo-space\index.html"
css_path = r"C:\Users\Pc\Downloads\minhngo-space\minhngo-space\minhngo-space\style.css"

# =========================================================================
# 1. UPDATE CSS FOR ABOUT & EXPERIENCE
# =========================================================================
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Make .about__head fit smoothly
css = re.sub(
    r"\.about__head\s*\{[^}]*\}",
    """.about__head {
    height: 101px;
    background: var(--coral);
    color: #fff;
    font-size: 42px;
    font-weight: 800;
    line-height: 101px;
    text-align: center;
    letter-spacing: -0.02em;
  }""",
    css,
    count=1
)

# Refine .about__bio line-height & font-size for rich professional copy
css = re.sub(
    r"\.about__bio\s*\{[^}]*\}",
    """.about__bio {
    left: 31px;
    top: 405px;
    width: 1050px;
    margin: 0;
    font-size: 16px;
    line-height: 27px;
  }""",
    css,
    count=1
)

# Refine .exp__job sizing so 5 detailed jobs fit with high readability
css = re.sub(
    r"\.exp__job\s*\{[^}]*\}",
    """.exp__job {
    display: grid;
    grid-template-columns: 296px 1fr;
    font-size: 17px;
    line-height: 30px;
  }""",
    css,
    count=1
)

css = re.sub(
    r"\.exp__job h3\s*\{[^}]*\}",
    """.exp__job h3 {
    margin: 0;
    font-size: 20px;
    font-weight: 700;
    line-height: 32px;
  }""",
    css,
    count=1
)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
print("CSS updated for About & Experience")

# =========================================================================
# 2. UPDATE HTML: ABOUT & EXPERIENCE MODAL
# =========================================================================
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

new_about_section = """      <!-- About me ⇄ Experience -->
      <section class="modal" data-modal="about" aria-label="About me">
        <div class="pop profile">
          <div class="profile__inner">

            <!-- Front Side: About Me Profile Card -->
            <article class="face about">
              <h2 class="about__head" style="margin:0">Software Developer &amp; AI Engineer</h2>
              <img class="about__abs about__photo" src="https://avatars.githubusercontent.com/u/262732549?v=4" alt="Muffaser Naeem's profile avatar">

              <p class="about__abs about__row about__name" style="margin:0"><b>Name:</b> Muffaser Naeem</p>
              <p class="about__abs about__row about__age" style="margin:0"><b>Location:</b> Lahore, Pakistan</p>
              <p class="about__abs about__row about__edu" style="margin:0"><b>Education:</b> COMSATS University Islamabad &middot; BS CS (Batch 29)</p>
              
              <ul class="about__abs about__list about__list--l">
                <li>Full-Stack Software Developer</li>
                <li>Applied AI &amp; Deep Learning Builder</li>
                <li>Hackathon Winner &amp; Open-Source Contributor</li>
              </ul>
              <ul class="about__abs about__list about__list--r">
                <li>Client-Side WASM &amp; Media Systems</li>
                <li>RESTful Microservices &amp; API Design</li>
                <li>Algorithmic Problem-Solving &amp; Clean Code</li>
              </ul>

              <p class="about__abs about__label about__tools-label" style="margin:0">Core Stack:</p>
              <div class="about__abs about__icons">
                <span>TypeScript</span>
                <span>Python</span>
                <span>JavaScript</span>
                <span>PyTorch</span>
                <span>C++</span>
              </div>

              <p class="about__abs about__label about__social-label" style="margin:0">Connect:</p>
              <div class="about__abs about__social">
                <a href="https://github.com/muffasernaeem302" data-link="github" target="_blank" rel="noopener" aria-label="GitHub">GitHub ↗</a>
                <a href="https://www.linkedin.com/in/muffaser-naeem-943475382/" data-link="linkedin" target="_blank" rel="noopener" aria-label="LinkedIn">LinkedIn ↗</a>
              </div>

              <p class="about__abs about__bio">I am a Software Developer and AI Engineer pursuing a Bachelor of Science in Computer Science at COMSATS University Islamabad. Driven by a builder mindset, I design and engineer scalable web applications, applied AI systems, and high-performance developer utilities. My recent work includes civic intelligence platforms with automated computer vision triage (FixMyCity), clinical conversational AI agents (DentalAI), from-scratch deep learning transformer models (Mini-GPT), and privacy-preserving client-side media engines (OMNI Compression). I bridge modern software craftsmanship with practical AI, focused on writing clean, maintainable code that solves real-world challenges.</p>

              <div class="about__abs about__more">
                <button class="linkish" data-flip="exp">
                  <span>View Education, Technical Experience &amp; Full Skills</span>
                  <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10h14M11 4l6 6-6 6"></path></svg>
                </button>
              </div>
            </article>

            <!-- Back Side: Experience, Education, and Skills Card -->
            <article class="face exp" aria-label="Experience & Background">
              <div class="exp__scroll">
                
                <!-- Education -->
                <div class="exp__job">
                  <div class="exp__when">
                    <h3>Education</h3>
                    <p>2024 &ndash; Present</p>
                    <p style="font-size:14px; opacity:0.85;">Lahore, Pakistan</p>
                  </div>
                  <div>
                    <h3>COMSATS University Islamabad</h3>
                    <ul>
                      <li><b>Degree:</b> Bachelor of Science in Computer Science &mdash; Currently Enrolled (Batch 29).</li>
                      <li><b>Core Coursework:</b> Data Structures &amp; Algorithms, Object-Oriented Programming (C++/Java), Database Management Systems, Discrete Mathematics, Artificial Intelligence Foundations, Computer Architecture, and Software Engineering.</li>
                      <li><b>Academic Focus:</b> Practical software engineering, algorithmic efficiency, system design, and applied deep learning.</li>
                    </ul>
                  </div>
                </div>

                <!-- AI & Machine Learning Work -->
                <div class="exp__job">
                  <div class="exp__when">
                    <h3>Applied AI &amp; ML</h3>
                    <p>Research &amp; Production</p>
                    <p style="font-size:14px; opacity:0.85;">Deep Learning &amp; NLP</p>
                  </div>
                  <div>
                    <h3>Intelligent Systems &amp; Autonomous Applications</h3>
                    <ul>
                      <li><b>FixMyCity (Civic AI &amp; Hackathon Project):</b> Engineered an end-to-end municipal platform using Python, FastAPI, and computer vision to classify urban issues, score urgency, and cluster duplicates by ~70% via geo-location proximity and image perceptual hashing.</li>
                      <li><b>DentalAI Bot (Clinical Assistant):</b> Designed a conversational AI triage system with TypeScript and Python, featuring clinical safety guardrails, intent classification, and emergency detection heuristics.</li>
                      <li><b>Mini-GPT (Generative AI Architecture):</b> Built a decoder-only transformer language model from scratch in PyTorch, implementing multi-head causal self-attention, layer normalization, residual connections, and tokenization without third-party LLM frameworks.</li>
                    </ul>
                  </div>
                </div>

                <!-- Web & Developer Tools Work -->
                <div class="exp__job">
                  <div class="exp__when">
                    <h3>Software Dev</h3>
                    <p>Web &amp; Systems</p>
                    <p style="font-size:14px; opacity:0.85;">Client-Side &amp; APIs</p>
                  </div>
                  <div>
                    <h3>Full-Stack Applications &amp; Developer Utilities</h3>
                    <ul>
                      <li><b>OMNI Compression:</b> Developed an in-browser media compression engine in TypeScript using the Canvas 2D API and multithreaded WebAssembly (WASM) workers, reducing file sizes by 60&ndash;85% with 100% client-side privacy.</li>
                      <li><b>Git Pulse Finder:</b> Built a zero-dependency GitHub developer intelligence platform with modern JavaScript (ES2024+), client-side in-memory caching, and sub-100ms repository analytics.</li>
                      <li><b>TypeFlow:</b> Created an offline-first typing performance utility capturing microsecond-level keystroke intervals with the browser's Performance API and IndexedDB persistence.</li>
                      <li><b>VibeSync:</b> Integrated the Spotify Web API via OAuth 2.0 PKCE, calculating multidimensional acoustic distance matrices for automated mood-based playlist clustering.</li>
                    </ul>
                  </div>
                </div>

                <!-- Technical Skills Matrix -->
                <div class="exp__job">
                  <div class="exp__when">
                    <h3>Technical Stack</h3>
                    <p>Core Competencies</p>
                    <p style="font-size:14px; opacity:0.85;">Tools &amp; Paradigms</p>
                  </div>
                  <div>
                    <h3>Languages, Frameworks &amp; Engineering Paradigms</h3>
                    <ul>
                      <li><b>Languages:</b> TypeScript, Python, JavaScript (ES2024+), C++, SQL, HTML5 / CSS3.</li>
                      <li><b>AI &amp; Data:</b> PyTorch, Transformers, Computer Vision (CNNs), NLP, Vector Distance Clustering, Prompt Engineering, OpenAI APIs.</li>
                      <li><b>Frontend Architecture:</b> Modern Vanilla JS, React, Three.js (WebGL 3D &amp; Canvas 2D), WebAssembly (WASM), Web Workers, Responsive Design.</li>
                      <li><b>Backend &amp; Cloud:</b> FastAPI, Node.js, Express, RESTful API Architecture, OAuth 2.0 (PKCE), Asynchronous I/O.</li>
                      <li><b>Tooling &amp; Practices:</b> Git &amp; GitHub, Linux CLI, VS Code, Postman, Figma, Agile Iteration, Object-Oriented Design (OOP).</li>
                    </ul>
                  </div>
                </div>

                <!-- Professional Strengths & Availability -->
                <div class="exp__job">
                  <div class="exp__when">
                    <h3>Career Focus</h3>
                    <p>Availability</p>
                    <p style="font-size:14px; opacity:0.85;">Remote &amp; On-Site</p>
                  </div>
                  <div>
                    <h3>Engineering Philosophy &amp; Availability</h3>
                    <ul>
                      <li><b>Builder Mentality:</b> Rapid prototyping, learning by building, clean modular code, and thorough technical documentation.</li>
                      <li><b>Target Roles:</b> Actively open to Software Engineering, Full-Stack / Frontend Developer, and Applied AI / Machine Learning roles, internships, and high-impact collaborative projects.</li>
                    </ul>
                  </div>
                </div>

              </div>
            </article>

          </div>
        </div>

        <button class="back" data-flip="about">
          <svg viewBox="0 0 30 30" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M26 15H5M13 7l-8 8 8 8"></path></svg>
          back
        </button>
        <button class="pop close about-close" data-close="" style="--d:2" aria-label="Close">
          <svg viewBox="0 0 42 42" fill="none" stroke="currentColor" stroke-width="5.5" stroke-linecap="round"><path d="M4 4l34 34M38 4L4 38"></path></svg>
        </button>
      </section>"""

# Replace about section in html
pattern_about = r"<!-- About me ⇄ Experience -->\s*<section class=\"modal\" data-modal=\"about\".*?</section>"
html, count_about = re.subn(pattern_about, new_about_section, html, flags=re.DOTALL)
print(f"About section replaced: {count_about}")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("index.html successfully updated with professional About & Experience!")
