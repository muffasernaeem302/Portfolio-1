# Elaborate all projects in index.html and style.css
$htmlFile = "C:\Users\Pc\Downloads\minhngo-space\minhngo-space\index.html"
$cssFile = "C:\Users\Pc\Downloads\minhngo-space\minhngo-space\minhngo-space\style.css"

$html = Get-Content $htmlFile -Raw -Encoding UTF8
$css = Get-Content $cssFile -Raw -Encoding UTF8

# =========================================================================
# 1. ENHANCE CSS: Add scroll and clean formatting for rich project details
# =========================================================================
$cssAdditions = @'

/* Enhanced Project Showcase Details styling */
.project-showcase__details {
  max-height: 670px;
  overflow-y: auto;
  scrollbar-width: thin;
  scrollbar-color: rgba(255, 90, 31, 0.4) transparent;
}
.project-showcase__details::-webkit-scrollbar {
  width: 6px;
}
.project-showcase__details::-webkit-scrollbar-thumb {
  background: rgba(255, 90, 31, 0.35);
  border-radius: 4px;
}
.project-showcase__section {
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}
.project-showcase__section-title {
  margin: 0 0 8px;
  color: var(--accent);
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}
.project-showcase__section-text {
  margin: 0;
  color: var(--text-2);
  font-size: 15px;
  line-height: 1.6;
}
.project-showcase__highlights {
  margin: 8px 0 0;
  padding-left: 18px;
  color: var(--text-2);
  font-size: 14px;
  line-height: 1.6;
}
.project-showcase__highlights li {
  margin-bottom: 5px;
}

/* Enhanced GitHub Project Cards for Apps and Brand modals */
.github-project {
  min-height: 380px;
}
.github-project-section {
  margin-top: 12px;
  padding-top: 10px;
  border-top: 1px solid #ebe8e0;
}
.github-project-section-title {
  display: block;
  margin-bottom: 4px;
  color: #a75442;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}
.github-project-section p {
  margin: 0;
  color: #4b4e56;
  font-size: 13.5px;
  line-height: 1.55;
}
.github-project-section ul {
  margin: 4px 0 0;
  padding-left: 16px;
  color: #4b4e56;
  font-size: 13px;
  line-height: 1.5;
}
.github-project-section ul li {
  margin-bottom: 3px;
}
.github-project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 10px;
}
.github-project-tag {
  display: inline-block;
  padding: 3px 8px;
  border-radius: 6px;
  background: #ede9df;
  color: #3b3d45;
  font-size: 11px;
  font-weight: 600;
}
'@

if (-not ($css -match "Enhanced Project Showcase Details styling")) {
  $css += "`r`n" + $cssAdditions
  Set-Content $cssFile -Value $css -Encoding UTF8 -NoNewline
  Write-Host "Updated style.css with enhanced project styles"
}

Write-Host "CSS update completed successfully"
