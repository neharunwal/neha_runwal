from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
RESUME_DIR = ROOT / "resume"
RESUME_DIR.mkdir(parents=True, exist_ok=True)
PDF_PATH = RESUME_DIR / "neha-runwal-resume.pdf"

styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="HeroName",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=24,
        leading=28,
        textColor=colors.HexColor("#142039"),
        spaceAfter=6,
    )
)
styles.add(
    ParagraphStyle(
        name="Subhead",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=11.2,
        leading=14,
        textColor=colors.HexColor("#3E567E"),
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        name="Meta",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9.2,
        leading=12,
        textColor=colors.HexColor("#6B748A"),
        spaceAfter=10,
    )
)
styles.add(
    ParagraphStyle(
        name="SectionTitle",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12.6,
        leading=15,
        textColor=colors.HexColor("#1A3C70"),
        spaceBefore=8,
        spaceAfter=7,
    )
)
styles.add(
    ParagraphStyle(
        name="RoleTitle",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=11.1,
        leading=13,
        textColor=colors.HexColor("#1C273F"),
        spaceAfter=5,
    )
)
styles["BodyText"].fontName = "Helvetica"
styles["BodyText"].fontSize = 10.2
styles["BodyText"].leading = 13.8
styles["BodyText"].textColor = colors.HexColor("#39465E")


def bullet_list(items):
    return ListFlowable(
        [ListItem(Paragraph(item, styles["BodyText"])) for item in items],
        bulletType="bullet",
        start="circle",
        leftIndent=14,
        bulletFontName="Helvetica",
        bulletFontSize=8,
    )


doc = SimpleDocTemplate(
    str(PDF_PATH),
    pagesize=letter,
    rightMargin=0.6 * inch,
    leftMargin=0.6 * inch,
    topMargin=0.55 * inch,
    bottomMargin=0.55 * inch,
)

story = [
    Paragraph("Neha Runwal", styles["HeroName"]),
    Paragraph(
        "Product-minded engineer | Enterprise builder | AI and machine learning learner",
        styles["Subhead"],
    ),
    Paragraph(
        "Sunnyvale, California, United States | LinkedIn: linkedin.com/in/neha-runwal-824b4817 | Portfolio created with Codex",
        styles["Meta"],
    ),
    Paragraph("Professional Summary", styles["SectionTitle"]),
    Paragraph(
        "Engineer and builder with publicly visible experience across PayPal, Infosys, and Bloomintek. Combines enterprise delivery instincts, practical internal tooling experience, and product-oriented web thinking. Over the last year, has been actively learning machine learning, exploring AI tools, and experimenting with vibe coding workflows to expand the way software gets designed and shipped.",
        styles["BodyText"],
    ),
    Spacer(1, 0.12 * inch),
]

strength_table = Table(
    [
        [
            Paragraph("<b>Core Strengths</b>", styles["BodyText"]),
            Paragraph("<b>Selected Technologies and Domains</b>", styles["BodyText"]),
        ],
        [
            bullet_list(
                [
                    "Enterprise engineering and internal tools",
                    "Product and startup problem solving",
                    "Fast execution under deadlines",
                    "Cross-disciplinary innovation thinking",
                    "AI-forward learning mindset",
                ]
            ),
            bullet_list(
                [
                    "Perl, HTML, Shell Scripting",
                    "Web Development, Web Design, SaaS Development",
                    "Artificial Intelligence, Machine Learning, Deep Learning",
                    "Bioinformatics, Data Science, Intelligent Systems",
                    "AI tools, prompt workflows, vibe coding, Codex",
                ]
            ),
        ],
    ],
    colWidths=[3.05 * inch, 3.05 * inch],
)
strength_table.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#D7E8FF")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#142039")),
            ("GRID", (0, 0), (-1, -1), 0.6, colors.HexColor("#B5C7E8")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("PADDING", (0, 0), (-1, -1), 8),
        ]
    )
)
story += [strength_table, Spacer(1, 0.12 * inch)]

story += [Paragraph("Experience and Career Highlights", styles["SectionTitle"])]

experience_sections = [
    (
        "Bloomintek | Product-focused software environment",
        [
            "Associated with a company building software, web, branding, and SaaS experiences.",
            "Brings a builder mindset centered on user experience, digital products, and execution velocity.",
        ],
    ),
    (
        "PayPal | Enterprise software experience",
        [
            "Public profile summary references more than two years of experience at PayPal.",
            "Recognized with the Blue Moon Award for the Risk Sandbox project tied to Q3-Q4 2012 work.",
        ],
    ),
    (
        "Infosys | Early engineering impact",
        [
            "Received the Bravo Award for creating a Weekend Support Tool in three days.",
            "Work explicitly referenced Perl, HTML, and shell scripting.",
        ],
    ),
]

for title, items in experience_sections:
    story.append(Paragraph(title, styles["RoleTitle"]))
    story.append(bullet_list(items))
    story.append(Spacer(1, 0.06 * inch))

story += [
    Paragraph("Education and Learning", styles["SectionTitle"]),
    Paragraph(
        "University of Cincinnati - College of Engineering and Applied Science | 2021-2022",
        styles["RoleTitle"],
    ),
    bullet_list(
        [
            "Graduate Incentive Award: 30% tuition-waiver scholarship.",
            "Relevant coursework included Artificial Intelligence, Machine Learning, Deep Learning, Bioinformatics, Data Science for Biomedical Research, Intelligent Systems, Intelligent Data Analysis, Innovation Design Thinking, and Interdisciplinary Innovation for Engineers.",
            "Over the last year: focused on machine learning, AI tools, and vibe coding exploration.",
        ]
    ),
    Spacer(1, 0.08 * inch),
    Paragraph("Awards and Recognition", styles["SectionTitle"]),
    bullet_list(
        [
            "Blue Moon Award, PayPal (June 2013) for the Risk Sandbox project.",
            "Bravo Award, Infosys (October 2009) for a Weekend Support Tool built in three days.",
            "FlyOhio Innovation Challenge 2021 - Second Place (Judges' choice) for a drone ecosystem innovation proposal.",
            "Graduate Incentive Award, University of Cincinnati (August 2020).",
        ]
    ),
    Spacer(1, 0.08 * inch),
    Paragraph(
        "<b>Note:</b> This resume was assembled from publicly visible professional information and the candidate's explicitly provided current AI/ML learning direction.",
        styles["BodyText"],
    ),
]

doc.build(story)
print(PDF_PATH)
