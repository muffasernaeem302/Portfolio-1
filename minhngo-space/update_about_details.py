# -*- coding: utf-8 -*-
import re

html_path = r"C:\Users\Pc\Downloads\minhngo-space\minhngo-space\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Enhanced About & Experience with rich details from GitHub & LinkedIn
# Keeping the EXACT original CSS classes, coordinates, and structure so NOTHING overlaps!
new_about_modal = """      <!-- About me ⇄ Experience -->
      <section class="modal" data-modal="about" aria-label="About me">
        <div class="pop profile">
          <div class="profile__inner">

            <article class="face about">
              <h2 class="about__head" style="margin:0">Software &amp; AI Developer</h2>
              <img class="about__abs about__photo" src="https://avatars.githubusercontent.com/u/262732549?v=4" alt="Muffaser Naeem's GitHub profile avatar">

              <p class="about__abs about__row about__name" style="margin:0"><b>Name:</b> Muffaser Naeem</p>
              <p class="about__abs about__row about__age" style="margin:0"><b>Location:</b> Lahore, Pakistan</p>
              <p class="about__abs about__row about__edu" style="margin:0"><b>Education:</b> COMSATS University Islamabad</p>
              <ul class="about__abs about__list about__list--l">
                <li>Full-Stack &amp; AI Dev</li>
                <li>Open-source builder</li>
              </ul>
              <ul class="about__abs about__list about__list--r">
                <li>Civic AI &amp; Dev Tools</li>
                <li>Hackathon builder</li>
              </ul>

              <p class="about__abs about__label about__tools-label" style="margin:0">Tools:</p>
              <div class="about__abs about__icons">
                <span>TypeScript</span>
                <span>Python</span>
                <span>JavaScript</span>
                <span>C++</span>
              </div>

              <p class="about__abs about__label about__social-label" style="margin:0">Social</p>
              <div class="about__abs about__social">
                <a href="https://github.com/muffasernaeem302" data-link="github" target="_blank" rel="noopener" aria-label="GitHub">GitHub</a>
                <a href="https://www.linkedin.com/in/muffaser-naeem-943475382/" data-link="linkedin" target="_blank" rel="noopener" aria-label="LinkedIn">LinkedIn</a>
              </div>

              <p class="about__abs about__bio">Software Developer and AI Engineer based in Lahore, studying at COMSATS University. I build practical, open-source projects on GitHub&mdash;from civic intelligence platforms (FixMyCity) and AI assistants (DentalAI) to client-side media engines (OMNI) and deep learning models (Mini-GPT). Let's connect on LinkedIn!</p>

              <div class="about__abs about__more">
                <button class="linkish" data-flip="exp">
                  <span>view experience &amp; skills</span>
                  <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10h14M11 4l6 6-6 6"></path></svg>
                </button>
              </div>
            </article>

            <article class="face exp" aria-label="Experience">
              <div class="exp__scroll">
                
                <div class="exp__job">
                  <div class="exp__when">
                    <h3>Education</h3>
                    <p>2024 &ndash; Present</p>
                    <p style="font-size:14px; opacity:0.8;">Lahore, Pakistan</p>
                  </div>
                  <div>
                    <h3>COMSATS University Islamabad</h3>
                    <ul>
                      <li><b>Degree:</b> BS in Computer Science &mdash; Currently Enrolled (Batch 29).</li>
                      <li><b>Relevant Coursework:</b> Data Structures &amp; Algorithms, Object-Oriented Programming (C++/Java), Database Systems, Artificial Intelligence Fundamentals, and Software Engineering.</li>
                      <li><b>Academic Focus:</b> Practical software engineering, algorithmic efficiency, system design, and applied deep learning.</li>
                    </ul>
                  </div>
                </div>

                <div class="exp__job">
                  <div class="exp__when">
                    <h3>GitHub</h3>
                    <p>Open Source</p>
                    <p style="font-size:14px; opacity:0.8;">7+ Public Repos</p>
                  </div>
                  <div>
                    <h3>Open-Source Projects &amp; Contributions</h3>
                    <ul>
                      <li><b>FixMyCity (Civic AI &amp; Hackathon):</b> Civic reporting platform with computer vision classification and geospatial de-duplication (~70% reduction in duplicate reports).</li>
                      <li><b>DentalAI Bot (Clinical Assistant):</b> Conversational AI triage system with medical safety guardrails and multi-turn symptom memory.</li>
                      <li><b>Mini-GPT (Transformer Research):</b> From-scratch PyTorch transformer language model exploring causal self-attention, layer normalization, and tokenization.</li>
                      <li><b>Developer Tools:</b> Built Git Pulse Finder (ecosystem analytics), OMNI Compression (client-side WASM engine), TypeFlow (offline-first speed trainer), and VibeSync (Spotify mood clustering).</li>
                    </ul>
                  </div>
                </div>

                <div class="exp__job">
                  <div class="exp__when">
                    <h3>LinkedIn</h3>
                    <p>Professional</p>
                    <p style="font-size:14px; opacity:0.8;">Open to Roles</p>
                  </div>
                  <div>
                    <h3>Software Engineering &amp; AI Focus</h3>
                    <ul>
                      <li><b>Profile:</b> Software Developer and AI Engineer passionate about end-to-end product development and learning by shipping real software.</li>
                      <li><b>Engineering Philosophy:</b> Writing clean, modular, and maintainable code with clear documentation and intuitive UX.</li>
                      <li><b>Availability:</b> Open to software engineering internships, junior developer roles, and impactful collaborative projects (remote &amp; on-site).</li>
                    </ul>
                  </div>
                </div>

                <div class="exp__job">
                  <div class="exp__when">
                    <h3>Tech Stack</h3>
                    <p>Competencies</p>
                    <p style="font-size:14px; opacity:0.8;">Tools &amp; Paradigms</p>
                  </div>
                  <div>
                    <h3>Languages, Frameworks &amp; Tools</h3>
                    <ul>
                      <li><b>Languages:</b> TypeScript, Python, JavaScript (ES2024+), C++, SQL, HTML5 / CSS3.</li>
                      <li><b>AI &amp; Data:</b> PyTorch, Transformers, Computer Vision (CNNs), NLP, Vector Clustering, Prompt Engineering, OpenAI APIs.</li>
                      <li><b>Frontend &amp; Backend:</b> Modern Vanilla JS, React, Three.js, Canvas 2D, WebAssembly (WASM), FastAPI, Node.js, REST APIs, OAuth 2.0 PKCE.</li>
                      <li><b>Tools &amp; Workflow:</b> Git, GitHub, VS Code, Postman, Linux CLI, Figma.</li>
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

pattern_about = r"<!-- About me ⇄ Experience -->\s*<section class=\"modal\" data-modal=\"about\".*?</section>"
html, count = re.subn(pattern_about, new_about_modal, html, flags=re.DOTALL)
print(f"About section updated: {count}")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("index.html successfully updated with GitHub & LinkedIn details!")
