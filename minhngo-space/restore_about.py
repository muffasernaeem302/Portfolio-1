# -*- coding: utf-8 -*-
import re

html_path = r"C:\Users\Pc\Downloads\minhngo-space\minhngo-space\index.html"
css_path = r"C:\Users\Pc\Downloads\minhngo-space\minhngo-space\minhngo-space\style.css"

# =========================================================================
# 1. RESTORE STYLE.CSS
# =========================================================================
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Remove the PERFECT ABOUT CARD LAYOUT block
css = re.sub(r"/\* =+ PERFECT ABOUT CARD LAYOUT.*", "", css, flags=re.DOTALL)

# Restore .about__head
css = re.sub(
    r"\.about__head\s*\{[^}]*\}",
    """.about__head {
    height: 101px;
    background: var(--coral);
    color: #fff;
    font-size: 63px;
    font-weight: 800;
    line-height: 101px;
    text-align: center;
    letter-spacing: 0.2px;
  }""",
    css,
    count=1
)

# Restore .about__bio
css = re.sub(
    r"\.about__bio\s*\{[^}]*\}",
    """.about__bio {
    left: 31px;
    top: 412px;
    width: 1050px;
    margin: 0;
    font-size: 18px;
    line-height: 40px;
  }""",
    css,
    count=1
)

# Restore .exp__job
css = re.sub(
    r"\.exp__job\s*\{[^}]*\}",
    """.exp__job {
    display: grid;
    grid-template-columns: 296px 1fr;
    font-size: 24px;
    line-height: 40px;
  }""",
    css,
    count=1
)

css = re.sub(
    r"\.exp__job h3\s*\{[^}]*\}",
    """.exp__job h3 {
    margin: 0;
    font-size: 24px;
    font-weight: 700;
    line-height: 40px;
  }""",
    css,
    count=1
)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
print("style.css successfully restored!")

# =========================================================================
# 2. RESTORE ABOUT SECTION IN INDEX.HTML
# =========================================================================
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

original_about_section = """      <!-- About me ⇄ Experience -->
      <section class="modal" data-modal="about" aria-label="About me">
        <div class="pop profile">
          <div class="profile__inner">

            <article class="face about">
              <h2 class="about__head" style="margin:0">Software Developer</h2>
              <img class="about__abs about__photo" src="https://avatars.githubusercontent.com/u/262732549?v=4" alt="Muffaser Naeem's GitHub profile avatar">

              <p class="about__abs about__row about__name" style="margin:0"><b>Name:</b> Muffaser Naeem</p>
              <p class="about__abs about__row about__age" style="margin:0"><b>Location:</b> Lahore, Pakistan</p>
              <p class="about__abs about__row about__edu" style="margin:0"><b>Affiliation:</b> COMSATS</p>
              <ul class="about__abs about__list about__list--l">
                <li>Open-source builder</li>
                <li>Web &amp; product dev</li>
              </ul>
              <ul class="about__abs about__list about__list--r">
                <li>AI &amp; interactive apps</li>
                <li>Problem-solving mindset</li>
              </ul>

              <p class="about__abs about__label about__tools-label" style="margin:0">Tools:</p>
              <div class="about__abs about__icons">
                <span>JavaScript</span>
                <span>TypeScript</span>
                <span>Python</span>
                <span>C++</span>
              </div>

              <p class="about__abs about__label about__social-label" style="margin:0">Social</p>
              <div class="about__abs about__social">
                <a href="https://github.com/muffasernaeem302" data-link="github" target="_blank" rel="noopener" aria-label="GitHub">GitHub</a>
                <a href="https://www.linkedin.com/in/muffaser-naeem-943475382/" data-link="linkedin" target="_blank" rel="noopener" aria-label="LinkedIn">LinkedIn</a>
              </div>

              <p class="about__abs about__bio">“A little bit curious” is how I describe myself. I’m a software developer based in Lahore who learns by building: from web tools and interactive apps to AI experiments and practical problem-solving projects. I’m especially interested in making technology useful, approachable, and fun to explore.</p>

              <div class="about__abs about__more">
                <button class="linkish" data-flip="exp">
                  <span>view experience</span>
                  <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10h14M11 4l6 6-6 6"></path></svg>
                </button>
              </div>
            </article>

            <article class="face exp" aria-label="Experience">
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
html, count = re.subn(pattern_about, original_about_section, html, flags=re.DOTALL)
print(f"About section restored in index.html: {count}")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Restoration complete!")
