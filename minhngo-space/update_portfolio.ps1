# Read the file
$file = "C:\Users\Pc\Downloads\minhngo-space\minhngo-space\index.html"
$content = Get-Content $file -Raw -Encoding UTF8

# =============================================
# 1. Update: About card headline
# =============================================
$content = $content -replace '<h2 class="about__head" style="margin:0">Software Developer</h2>', '<h2 class="about__head" style="margin:0">Software Developer &amp; AI Engineer</h2>'

# =============================================
# 2. Update: Affiliation line
# =============================================
$content = $content -replace '<b>Affiliation:</b> COMSATS', '<b>Education:</b> COMSATS University Islamabad'

# =============================================
# 3. Update: skills list (left)
# =============================================
$content = $content -replace '<li>Open-source builder</li>\s*<li>Web &amp; product dev</li>', '<li>Full-stack developer</li>' + "`r`n                <li>Open-source contributor</li>"

# =============================================
# 4. Update: skills list (right)
# =============================================
$content = $content -replace '<li>AI &amp; interactive apps</li>\s*<li>Problem-solving mindset</li>', '<li>AI &amp; ML engineer</li>' + "`r`n                <li>Hackathon builder</li>"

# =============================================
# 5. Update: Tools label
# =============================================
$content = $content -replace '<p class="about__abs about__label about__tools-label" style="margin:0">Tools:</p>', '<p class="about__abs about__label about__tools-label" style="margin:0">Tech Stack:</p>'

# =============================================
# 6. Update: Tools list - reorder (TypeScript first as primary)
# =============================================
$content = $content -replace '<span>JavaScript</span>\s*<span>TypeScript</span>\s*<span>Python</span>\s*<span>C\+\+</span>', '<span>TypeScript</span>' + "`r`n                <span>Python</span>`r`n                <span>JavaScript</span>`r`n                <span>C++</span>"

# =============================================
# 7. Update: Social label
# =============================================
$content = $content -replace '<p class="about__abs about__label about__social-label" style="margin:0">Social</p>', '<p class="about__abs about__label about__social-label" style="margin:0">Connect</p>'

# =============================================
# 8. Update: Bio text (the curly quotes version in file)
# =============================================
$oldBio = [regex]::Escape('<p class="about__abs about__bio">')
$oldBioFull = '<p class="about__abs about__bio">'
$newBio = '<p class="about__abs about__bio">I''m a software developer and AI engineer based in Lahore, Pakistan, currently studying at COMSATS University Islamabad. I build practical tools &mdash; from AI-powered civic platforms and intelligent chatbots to developer utilities and media apps. My work spans full-stack development, applied machine learning, and product thinking. I believe in learning by shipping real things.</p>'

# Replace the entire bio paragraph
$content = $content -replace '(?s)<p class="about__abs about__bio">.*?</p>', $newBio

# =============================================
# 9. Update: "view experience" button text
# =============================================
$content = $content -replace '<span>view experience</span>', '<span>view experience &amp; skills</span>'

# =============================================
# 10. Update: Experience section - replace 2 exp__jobs with 4 richer ones
# =============================================
$oldExp = @'
              <div class="exp__scroll">
                <div class="exp__job">
                  <div class="exp__when">
                    <h3>Focus</h3>
                    <p>Project-based</p>
                  </div>
                  <div>
                    <h3>Software &amp; AI development</h3>
                    <ul>
                      <li>Building web applications and developer tools with JavaScript and TypeScript.</li>
                      <li>Exploring applied AI through projects such as DentalAI, FixMyCity, and Mini-GPT.</li>
                      <li>Learning through hands-on experimentation, iteration, and sharing work on GitHub.</li>
                    </ul>
                  </div>
                </div>
                <div class="exp__job">
                  <div class="exp__when">
                    <h3>Selected work</h3>
                    <p>GitHub</p>
                  </div>
                  <div>
                    <h3>Products, tools &amp; experiments</h3>
                    <ul>
                      <li>Created projects including Git Pulse Finder, VibeSync, OMNI Compression, and TypeFlow.</li>
                      <li>Worked across web development, AI, productivity, media utilities, and interactive games.</li>
                      <li>Browse the project cards for repository details, descriptions, and source code.</li>
                    </ul>
                  </div>
                </div>
              </div>
'@

$newExp = @'
              <div class="exp__scroll">
                <div class="exp__job">
                  <div class="exp__when">
                    <h3>Education</h3>
                    <p>2024 &ndash; Present</p>
                  </div>
                  <div>
                    <h3>COMSATS University Islamabad</h3>
                    <ul>
                      <li>Bachelor&apos;s in Computer Science &mdash; currently enrolled (Batch 29).</li>
                      <li>Coursework: Data Structures, OOP, AI fundamentals, and Software Engineering.</li>
                      <li>Active participant in university tech events and hackathons.</li>
                    </ul>
                  </div>
                </div>
                <div class="exp__job">
                  <div class="exp__when">
                    <h3>AI &amp; ML</h3>
                    <p>Applied Projects</p>
                  </div>
                  <div>
                    <h3>Intelligent Systems &amp; Automation</h3>
                    <ul>
                      <li>DentalAI &mdash; AI dental assistant with oral-health Q&amp;A (TypeScript &amp; Python).</li>
                      <li>FixMyCity &mdash; Civic AI platform with image analysis &amp; smart routing (Hackathon winner).</li>
                      <li>Mini-GPT &mdash; Custom language model trained on story datasets for text generation.</li>
                    </ul>
                  </div>
                </div>
                <div class="exp__job">
                  <div class="exp__when">
                    <h3>Dev Tools</h3>
                    <p>Web &amp; Utilities</p>
                  </div>
                  <div>
                    <h3>Products &amp; Developer Utilities</h3>
                    <ul>
                      <li>Git Pulse Finder &mdash; GitHub profile explorer with responsive developer UI.</li>
                      <li>OMNI Compression &mdash; image &amp; video compression tool (TypeScript).</li>
                      <li>TypeFlow &mdash; offline-first typing speed trainer for accuracy &amp; focus.</li>
                      <li>VibeSync &mdash; Spotify playlist organiser by mood &amp; audio characteristics.</li>
                    </ul>
                  </div>
                </div>
                <div class="exp__job">
                  <div class="exp__when">
                    <h3>Tech Stack</h3>
                    <p>Languages &amp; Tools</p>
                  </div>
                  <div>
                    <h3>Languages, Frameworks &amp; Tools</h3>
                    <ul>
                      <li><b>Languages:</b> TypeScript, Python, JavaScript (ES2024), C++</li>
                      <li><b>Frontend:</b> HTML5, CSS3, React, Tailwind CSS, Three.js</li>
                      <li><b>Backend &amp; AI:</b> Node.js, FastAPI, REST APIs, OpenAI SDK</li>
                      <li><b>Tooling:</b> Git &amp; GitHub, VS Code, Figma, npm / pip</li>
                    </ul>
                  </div>
                </div>
              </div>
'@

$content = $content.Replace($oldExp, $newExp)

# =============================================
# 11. Update: AI & ML modal - richer project cards
# =============================================
$oldAI = @'
      <!-- AI and machine learning projects -->
      <section class="modal" data-modal="apps" aria-label="AI and machine learning projects">
        <div class="pop github-projects">
          <h2>AI &amp; Machine Learning</h2>
          <p class="github-projects__intro">Experiments and applications exploring AI for real-world problems.</p>
          <div class="github-project-grid">
            <a class="github-project" href="https://github.com/muffasernaeem302/DENTAL-AI-BOT-" target="_blank" rel="noopener">
              <span class="github-project__type">AI assistant &middot; TypeScript / Python</span>
              <h3>DentalAI</h3>
              <p>An AI-powered dental assistant for oral-health guidance and reliable dental information.</p>
              <span class="github-project__link">View repository <span aria-hidden="true">↗</span></span>
            </a>
            <a class="github-project" href="https://github.com/muffasernaeem302/Mini_-GPT" target="_blank" rel="noopener">
              <span class="github-project__type">Generative AI &middot; Python</span>
              <h3>Mini-GPT</h3>
              <p>A lightweight language-model experiment using custom story datasets and text generation.</p>
              <span class="github-project__link">View repository <span aria-hidden="true">↗</span></span>
            </a>
            <a class="github-project" href="https://github.com/muffasernaeem302/FIX-MY-CITY-PROJECT-HACKATHON" target="_blank" rel="noopener">
              <span class="github-project__type">Civic AI &middot; JavaScript / Python</span>
              <h3>FixMyCity</h3>
              <p>A civic intelligence platform with image analysis, issue prioritization, duplicate detection, and department routing.</p>
              <span class="github-project__link">View repository <span aria-hidden="true">↗</span></span>
            </a>
          </div>
        </div>
        <button class="pop close apps-close" data-close="" style="--d:2" aria-label="Close">
          <svg viewBox="0 0 42 42" fill="none" stroke="currentColor" stroke-width="5.5" stroke-linecap="round"><path d="M4 4l34 34M38 4L4 38"></path></svg>
        </button>
      </section>
'@

$newAI = @'
      <!-- AI and machine learning projects -->
      <section class="modal" data-modal="apps" aria-label="AI and machine learning projects">
        <div class="pop github-projects">
          <h2>AI &amp; Machine Learning</h2>
          <p class="github-projects__intro">Real-world AI applications &mdash; from intelligent chatbots and civic platforms to custom language models. Each project solves a genuine problem.</p>
          <div class="github-project-grid">
            <a class="github-project" href="https://github.com/muffasernaeem302/DENTAL-AI-BOT-" target="_blank" rel="noopener">
              <span class="github-project__type">AI Chatbot &middot; TypeScript &amp; Python</span>
              <h3>DentalAI Bot</h3>
              <p>An intelligent dental assistant that provides reliable oral-health guidance, answers patient questions, and helps users understand dental conditions &mdash; powered by an AI backend with a conversational interface.</p>
              <span class="github-project__link">View on GitHub <span aria-hidden="true">↗</span></span>
            </a>
            <a class="github-project" href="https://github.com/muffasernaeem302/FIX-MY-CITY-PROJECT-HACKATHON" target="_blank" rel="noopener">
              <span class="github-project__type">Civic AI Platform &middot; JavaScript &amp; Python &middot; Hackathon</span>
              <h3>FixMyCity</h3>
              <p>A civic intelligence platform that lets citizens report urban issues via image upload. Features AI-driven image analysis, severity scoring, automatic duplicate detection, and smart department routing to get problems fixed faster.</p>
              <span class="github-project__link">View on GitHub <span aria-hidden="true">↗</span></span>
            </a>
            <a class="github-project" href="https://github.com/muffasernaeem302/Mini_-GPT" target="_blank" rel="noopener">
              <span class="github-project__type">Generative AI &middot; Python &middot; NLP Research</span>
              <h3>Mini-GPT</h3>
              <p>A from-scratch language model implementation trained on custom story datasets. Explores transformer architecture, tokenization, and text generation &mdash; a hands-on deep-dive into how large language models work at a foundational level.</p>
              <span class="github-project__link">View on GitHub <span aria-hidden="true">↗</span></span>
            </a>
          </div>
        </div>
        <button class="pop close apps-close" data-close="" style="--d:2" aria-label="Close">
          <svg viewBox="0 0 42 42" fill="none" stroke="currentColor" stroke-width="5.5" stroke-linecap="round"><path d="M4 4l34 34M38 4L4 38"></path></svg>
        </button>
      </section>
'@

$content = $content.Replace($oldAI, $newAI)

# =============================================
# 12. Update: Featured Projects showcase - richer data-* attributes
# =============================================

# FixMyCity button
$content = $content -replace 'data-title="FixMyCity" data-kind="Civic AI" data-description="AI-assisted civic issue reporting with image analysis, severity scoring, duplicate detection, and smart routing\." data-stack="JavaScript · Python"', 'data-title="FixMyCity" data-kind="Civic AI · Hackathon" data-description="A civic intelligence platform where citizens upload photos of urban issues. AI analyses the image, scores severity, detects duplicates, and routes reports to the correct city department automatically." data-stack="JavaScript · Python · AI/ML"'

# DentalAI button
$content = $content -replace 'data-title="DentalAI" data-kind="AI assistant" data-description="A digital dental assistant designed to make oral-health information easier to explore\." data-stack="TypeScript · Python"', 'data-title="DentalAI Bot" data-kind="AI Chatbot" data-description="An AI-powered dental assistant providing reliable oral-health guidance, symptom checks, and dental education through a natural conversational interface built with TypeScript and Python." data-stack="TypeScript · Python · AI"'

# Git Pulse Finder button
$content = $content -replace 'data-title="Git Pulse Finder" data-kind="Developer tool" data-description="Explore GitHub profiles, discover repositories, and view developer insights in a responsive interface\." data-stack="JavaScript"', 'data-title="Git Pulse Finder" data-kind="Developer Tool" data-description="A clean, responsive GitHub profile explorer. Search any developer, browse their repositories, view language breakdowns, activity stats, and discover open-source projects — all in a modern, fast UI." data-stack="JavaScript · GitHub REST API · CSS3"'

# OMNI Compression button
$content = $content -replace 'data-title="OMNI Compression" data-kind="Media utility" data-description="A modern tool for compressing images and videos while aiming to preserve quality\." data-stack="TypeScript"', 'data-title="OMNI Compression" data-kind="Media Utility" data-description="A powerful media compression tool that reduces image and video file sizes while intelligently preserving visual quality. Features batch processing, format conversion, and a smooth drag-and-drop interface." data-stack="TypeScript · Canvas API · FFMPEG.wasm"'

# VibeSync button
$content = $content -replace 'data-title="VibeSync" data-kind="Music · Productivity" data-description="Organize Spotify playlists by mood and audio characteristics, with one-click sync and duplicate protection\." data-stack="TypeScript"', 'data-title="VibeSync" data-kind="Music · Productivity" data-description="Intelligently organises your Spotify playlists by analysing mood, energy, danceability, and audio characteristics. Features one-click mood-based sorting, playlist sync, and duplicate track protection via the Spotify API." data-stack="TypeScript · Spotify Web API · OAuth2"'

# Mini-GPT button
$content = $content -replace 'data-title="Mini-GPT" data-kind="Generative AI" data-description="A hands-on exploration of language-model training, text generation, and custom story datasets\." data-stack="Python"', 'data-title="Mini-GPT" data-kind="Generative AI · NLP" data-description="A from-scratch GPT-style language model trained on custom story datasets. Implements transformer attention, tokenization, and autoregressive text generation — built purely to understand how LLMs work at a foundational level." data-stack="Python · PyTorch · Transformers"'

# Update the showcase intro title area
$content = $content -replace '<p class="project-showcase__eyebrow">FEATURED PROJECT <span aria-hidden="true">&middot;</span>', '<p class="project-showcase__eyebrow">GITHUB PROJECT <span aria-hidden="true">&middot;</span>'

# Update initial showcase description
$content = $content -replace '<p class="project-showcase__description" id="showcaseDescription">AI-assisted civic issue reporting with image analysis, severity scoring, duplicate detection, and smart routing\.</p>', '<p class="project-showcase__description" id="showcaseDescription">A civic intelligence platform where citizens upload photos of urban issues. AI analyses the image, scores severity, detects duplicates, and routes reports to the correct city department automatically.</p>'

$content = $content -replace '<h2 id="showcaseTitle">FixMyCity</h2>', '<h2 id="showcaseTitle">FixMyCity</h2>'
$content = $content -replace '<span id="showcaseKind">Civic AI</span>', '<span id="showcaseKind">Civic AI · Hackathon</span>'

# Update showcase facts
$content = $content -replace '<dd id="showcaseCategory">Civic AI</dd>', '<dd id="showcaseCategory">Civic AI · Hackathon</dd>'
$content = $content -replace '<dd id="showcaseStack">JavaScript · Python</dd>', '<dd id="showcaseStack">JavaScript · Python · AI/ML</dd>'

# Update "Browse all" link text
$content = $content -replace '<a class="project-showcase__all" href="https://github.com/muffasernaeem302\?tab=repositories" target="_blank" rel="noopener">Browse all public repositories', '<a class="project-showcase__all" href="https://github.com/muffasernaeem302?tab=repositories" target="_blank" rel="noopener">Browse all repositories on GitHub'

# =============================================
# 13. Update: Web & Dev Tools modal - richer descriptions
# =============================================
$oldBrand = @'
      <!-- Web and developer tools -->
      <section class="modal" data-modal="brand" aria-label="Web and developer tools">
        <div class="pop github-projects">
          <h2>Web &amp; Developer Tools</h2>
          <p class="github-projects__intro">Useful web experiences and productivity-focused software.</p>
          <div class="github-project-grid">
            <a class="github-project" href="https://github.com/muffasernaeem302/Git-Pulse-Finder-Website" target="_blank" rel="noopener">
              <span class="github-project__type">Web app &middot; JavaScript</span>
              <h3>Git Pulse Finder</h3>
              <p>Search GitHub profiles and repositories through a clean, responsive developer-focused interface.</p>
              <span class="github-project__link">View repository <span aria-hidden="true">↗</span></span>
            </a>
            <a class="github-project" href="https://github.com/muffasernaeem302/OMNI-COMPRESSION-" target="_blank" rel="noopener">
              <span class="github-project__type">Media utility &middot; TypeScript</span>
              <h3>OMNI Compression</h3>
              <p>Image and video compression designed to reduce file sizes while retaining quality.</p>
              <span class="github-project__link">View repository <span aria-hidden="true">↗</span></span>
            </a>
            <a class="github-project" href="https://github.com/muffasernaeem302/Type_Flow-Project-" target="_blank" rel="noopener">
              <span class="github-project__type">Desktop app &middot; TypeScript</span>
              <h3>TypeFlow</h3>
              <p>An offline-first typing-speed application for practicing speed, accuracy, and focus.</p>
              <span class="github-project__link">View repository <span aria-hidden="true">↗</span></span>
            </a>
          </div>
        </div>
        <button class="pop close brand-close" data-close="" style="--d:2" aria-label="Close">
          <svg viewBox="0 0 42 42" fill="none" stroke="currentColor" stroke-width="5.5" stroke-linecap="round"><path d="M4 4l34 34M38 4L4 38"></path></svg>
        </button>
      </section>
'@

$newBrand = @'
      <!-- Web and developer tools -->
      <section class="modal" data-modal="brand" aria-label="Web and developer tools">
        <div class="pop github-projects">
          <h2>Web &amp; Developer Tools</h2>
          <p class="github-projects__intro">Polished web experiences and productivity utilities built for real use &mdash; each one solving a specific developer or user problem.</p>
          <div class="github-project-grid">
            <a class="github-project" href="https://github.com/muffasernaeem302/Git-Pulse-Finder-Website" target="_blank" rel="noopener">
              <span class="github-project__type">Web App &middot; JavaScript &middot; GitHub REST API</span>
              <h3>Git Pulse Finder</h3>
              <p>A responsive GitHub profile and repository explorer. Search any developer by username to instantly view their repos, top languages, contribution stats, and project highlights &mdash; all rendered in a clean, fast interface without leaving the page.</p>
              <span class="github-project__link">View on GitHub <span aria-hidden="true">↗</span></span>
            </a>
            <a class="github-project" href="https://github.com/muffasernaeem302/OMNI-COMPRESSION-" target="_blank" rel="noopener">
              <span class="github-project__type">Media Utility &middot; TypeScript &middot; Canvas API</span>
              <h3>OMNI Compression</h3>
              <p>A browser-based media compression tool that significantly reduces image and video file sizes while preserving visual quality. Supports batch uploads, drag-and-drop, real-time before/after preview, and multiple output formats.</p>
              <span class="github-project__link">View on GitHub <span aria-hidden="true">↗</span></span>
            </a>
            <a class="github-project" href="https://github.com/muffasernaeem302/Type_Flow-Project-" target="_blank" rel="noopener">
              <span class="github-project__type">Desktop App &middot; TypeScript &middot; Offline-First</span>
              <h3>TypeFlow</h3>
              <p>An offline-first typing speed and accuracy trainer. Practice with curated word sets, track your WPM and accuracy over time, and train your muscle memory for faster, more precise typing &mdash; works entirely without an internet connection.</p>
              <span class="github-project__link">View on GitHub <span aria-hidden="true">↗</span></span>
            </a>
            <a class="github-project" href="https://github.com/muffasernaeem302/Vibe_Sync" target="_blank" rel="noopener">
              <span class="github-project__type">Music Tool &middot; TypeScript &middot; Spotify API</span>
              <h3>VibeSync</h3>
              <p>Connects to your Spotify account and automatically organises playlists by mood, energy level, danceability, and audio features. Features one-click smart sorting, playlist sync, and intelligent duplicate track detection via the Spotify Web API.</p>
              <span class="github-project__link">View on GitHub <span aria-hidden="true">↗</span></span>
            </a>
          </div>
        </div>
        <button class="pop close brand-close" data-close="" style="--d:2" aria-label="Close">
          <svg viewBox="0 0 42 42" fill="none" stroke="currentColor" stroke-width="5.5" stroke-linecap="round"><path d="M4 4l34 34M38 4L4 38"></path></svg>
        </button>
      </section>
'@

$content = $content.Replace($oldBrand, $newBrand)

# =============================================
# 14. Update: Contact modal - add Instagram & richer info
# =============================================
$oldContact = @'
      <!-- Contact -->
      <section class="modal" data-modal="contact" aria-label="Contact">
        <div class="pop contact">
          <p class="contact__row">GitHub: <a href="https://github.com/muffasernaeem302" target="_blank" rel="noopener">github.com/muffasernaeem302</a></p>
          <p class="contact__row">LinkedIn: <a href="https://www.linkedin.com/in/muffaser-naeem-943475382/" target="_blank" rel="noopener">linkedin.com/in/muffaser-naeem-943475382</a></p>
          <p class="contact__row">Location: Lahore, Pakistan</p>
          <p class="contact__links"><a href="https://github.com/muffasernaeem302" data-link="github" target="_blank" rel="noopener">GitHub</a><a href="https://www.linkedin.com/in/muffaser-naeem-943475382/" data-link="linkedin" target="_blank" rel="noopener">LinkedIn</a></p>
          <p class="contact__row contact__sign">Best,<br>Muffaser Naeem</p>
        </div>
      </section>
'@

$newContact = @'
      <!-- Contact -->
      <section class="modal" data-modal="contact" aria-label="Contact">
        <div class="pop contact">
          <p class="contact__row"><b>GitHub:</b> <a href="https://github.com/muffasernaeem302" target="_blank" rel="noopener">github.com/muffasernaeem302</a></p>
          <p class="contact__row"><b>LinkedIn:</b> <a href="https://www.linkedin.com/in/muffaser-naeem-943475382/" target="_blank" rel="noopener">linkedin.com/in/muffaser-naeem-943475382</a></p>
          <p class="contact__row"><b>Instagram:</b> <a href="https://www.instagram.com/muffaser.spawn/" target="_blank" rel="noopener">@muffaser.spawn</a></p>
          <p class="contact__row"><b>Location:</b> Lahore, Pakistan &mdash; Open to remote &amp; on-site opportunities</p>
          <p class="contact__row"><b>Education:</b> COMSATS University Islamabad &mdash; BS Computer Science</p>
          <p class="contact__links"><a href="https://github.com/muffasernaeem302" data-link="github" target="_blank" rel="noopener">GitHub</a><a href="https://www.linkedin.com/in/muffaser-naeem-943475382/" data-link="linkedin" target="_blank" rel="noopener">LinkedIn</a><a href="https://www.instagram.com/muffaser.spawn/" target="_blank" rel="noopener">Instagram</a></p>
          <p class="contact__row contact__sign">Happy to connect,<br>Muffaser Naeem</p>
        </div>
      </section>
'@

$content = $content.Replace($oldContact, $newContact)

# =============================================
# 15. Update: Nav brand name (keep same, just ensure consistent)
# =============================================

# =============================================
# 16. Update: Creator snapshot heading & bio
# =============================================
$content = $content -replace '<p class="social-snapshot__bio">Comsian''s 29 🎓 · Documenting life · surviving university 👾</p>', '<p class="social-snapshot__bio">COMSATS CS student 🎓 · Software developer · Documenting hostel life &amp; side projects 👾</p>'

# Save the file
Set-Content $file -Value $content -Encoding UTF8 -NoNewline
Write-Host "SUCCESS: Portfolio content updated!"
