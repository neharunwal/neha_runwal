from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parent
RESUME_DIR = ROOT / "resume"
RESUME_DIR.mkdir(parents=True, exist_ok=True)
DOCX_PATH = RESUME_DIR / "neha-runwal-resume.docx"


def set_cell_shading(cell, color):
    tc_pr = cell._tc.get_or_add_tcPr()
    shading = OxmlElement("w:shd")
    shading.set(qn("w:fill"), color)
    tc_pr.append(shading)


def set_margins(section, top, right, bottom, left):
    section.top_margin = Inches(top)
    section.right_margin = Inches(right)
    section.bottom_margin = Inches(bottom)
    section.left_margin = Inches(left)


doc = Document()
section = doc.sections[0]
set_margins(section, 0.55, 0.65, 0.55, 0.65)

styles = doc.styles
styles["Normal"].font.name = "Aptos"
styles["Normal"].font.size = Pt(10.5)

title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.LEFT
run = title.add_run("Neha Runwal")
run.font.size = Pt(25)
run.font.bold = True
run.font.color.rgb = RGBColor(20, 31, 57)

subtitle = doc.add_paragraph()
subtitle.space_after = Pt(6)
subtitle_run = subtitle.add_run(
    "Product-minded engineer | Enterprise builder | AI and machine learning learner"
)
subtitle_run.font.size = Pt(11.5)
subtitle_run.font.color.rgb = RGBColor(62, 86, 126)

meta = doc.add_paragraph()
meta.space_after = Pt(12)
meta_run = meta.add_run(
    "Sunnyvale, California, United States  |  LinkedIn: linkedin.com/in/neha-runwal-824b4817  |  Portfolio created with Codex"
)
meta_run.font.size = Pt(9.5)
meta_run.font.color.rgb = RGBColor(94, 104, 124)

summary_heading = doc.add_paragraph()
summary_heading_run = summary_heading.add_run("Professional Summary")
summary_heading_run.bold = True
summary_heading_run.font.size = Pt(12.5)
summary_heading_run.font.color.rgb = RGBColor(26, 60, 112)

summary = doc.add_paragraph()
summary.style = styles["Normal"]
summary.add_run(
    "Engineer and builder with publicly visible experience across PayPal, Infosys, and Bloomintek. "
    "Combines enterprise delivery instincts, practical internal tooling experience, and product-oriented web thinking. "
    "Over the last year, has been actively learning machine learning, exploring AI tools, and experimenting with vibe coding workflows to expand the way software gets designed and shipped."
)

table = doc.add_table(rows=1, cols=2)
table.style = "Table Grid"
table.autofit = True

hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Core Strengths"
hdr_cells[1].text = "Selected Technologies and Domains"
for cell in hdr_cells:
    set_cell_shading(cell, "D7E8FF")
    for paragraph in cell.paragraphs:
        for run in paragraph.runs:
            run.bold = True
            run.font.color.rgb = RGBColor(20, 31, 57)

row = table.add_row().cells
strengths = [
    "Enterprise engineering and internal tools",
    "Product and startup problem solving",
    "Fast execution under deadlines",
    "Cross-disciplinary innovation thinking",
    "AI-forward learning mindset",
]
techs = [
    "Perl, HTML, Shell Scripting",
    "Web Development, Web Design, SaaS Development",
    "Artificial Intelligence, Machine Learning, Deep Learning",
    "Bioinformatics, Data Science, Intelligent Systems",
    "AI tools, prompt workflows, vibe coding, Codex",
]

for item in strengths:
    row[0].add_paragraph(item, style="List Bullet")
for item in techs:
    row[1].add_paragraph(item, style="List Bullet")

exp_heading = doc.add_paragraph()
exp_heading.space_before = Pt(12)
exp_run = exp_heading.add_run("Experience and Career Highlights")
exp_run.bold = True
exp_run.font.size = Pt(12.5)
exp_run.font.color.rgb = RGBColor(26, 60, 112)

experiences = [
    (
        "Bloomintek",
        "Product-focused software environment",
        [
            "Associated with a company building software, web, branding, and SaaS experiences.",
            "Brings a builder mindset centered on user experience, digital products, and execution velocity.",
        ],
    ),
    (
        "PayPal",
        "Enterprise software experience",
        [
            "Public profile summary references more than two years of experience at PayPal.",
            "Recognized with the Blue Moon Award for the Risk Sandbox project tied to Q3-Q4 2012 work.",
        ],
    ),
    (
        "Infosys",
        "Early engineering impact",
        [
            "Received the Bravo Award for creating a Weekend Support Tool in three days.",
            "Work explicitly referenced Perl, HTML, and shell scripting.",
        ],
    ),
]

for company, role, bullets in experiences:
    p = doc.add_paragraph()
    p.space_before = Pt(6)
    r = p.add_run(company)
    r.bold = True
    r.font.size = Pt(11.2)
    p.add_run(f"  |  {role}")
    for bullet in bullets:
      doc.add_paragraph(bullet, style="List Bullet")

edu_heading = doc.add_paragraph()
edu_heading.space_before = Pt(10)
edu_run = edu_heading.add_run("Education and Learning")
edu_run.bold = True
edu_run.font.size = Pt(12.5)
edu_run.font.color.rgb = RGBColor(26, 60, 112)

edu = doc.add_paragraph()
edu.add_run("University of Cincinnati - College of Engineering and Applied Science").bold = True
edu.add_run("  |  2021-2022")
for bullet in [
    "Graduate Incentive Award: 30% tuition-waiver scholarship.",
    "Relevant coursework included Artificial Intelligence, Machine Learning, Deep Learning, Bioinformatics, Data Science for Biomedical Research, Intelligent Systems, Intelligent Data Analysis, Innovation Design Thinking, and Interdisciplinary Innovation for Engineers.",
    "Over the last year: focused on machine learning, AI tools, and vibe coding exploration.",
]:
    doc.add_paragraph(bullet, style="List Bullet")

award_heading = doc.add_paragraph()
award_heading.space_before = Pt(10)
award_run = award_heading.add_run("Awards and Recognition")
award_run.bold = True
award_run.font.size = Pt(12.5)
award_run.font.color.rgb = RGBColor(26, 60, 112)

for bullet in [
    "Blue Moon Award, PayPal (June 2013) for the Risk Sandbox project.",
    "Bravo Award, Infosys (October 2009) for a Weekend Support Tool built in three days.",
    "FlyOhio Innovation Challenge 2021 - Second Place (Judges' choice) for a drone ecosystem innovation proposal.",
    "Graduate Incentive Award, University of Cincinnati (August 2020).",
]:
    doc.add_paragraph(bullet, style="List Bullet")

closing = doc.add_paragraph()
closing.space_before = Pt(10)
closing.add_run("Note: ").bold = True
closing.add_run(
    "This resume was assembled from publicly visible professional information and the candidate's explicitly provided current AI/ML learning direction."
)

doc.save(DOCX_PATH)
print(DOCX_PATH)
