from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import ListFlowable, ListItem, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


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
        fontSize=12.3,
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
        fontSize=11,
        leading=13,
        textColor=colors.HexColor("#1C273F"),
        spaceAfter=5,
    )
)
styles["BodyText"].fontName = "Helvetica"
styles["BodyText"].fontSize = 10
styles["BodyText"].leading = 13.4
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
    rightMargin=0.55 * inch,
    leftMargin=0.55 * inch,
    topMargin=0.5 * inch,
    bottomMargin=0.5 * inch,
)

story = [
    Paragraph("Neha Runwal", styles["HeroName"]),
    Paragraph(
        "Product design, platform engineering, strategic planning, and AI-forward execution",
        styles["Subhead"],
    ),
    Paragraph(
        "Milpitas, CA | 408-219-7990 | NehaRunwal@gmail.com | linkedin.com/in/neha-runwal-824b4817 | Portfolio created with Codex",
        styles["Meta"],
    ),
    Paragraph("Summary", styles["SectionTitle"]),
    Paragraph(
        "17+ years of extensive experience in product design, strategic planning, development, and execution. Ready to take on challenges and improve user experience. Recent focus includes learning machine learning, exploring AI tools, and experimenting with vibe coding workflows.",
        styles["BodyText"],
    ),
    Spacer(1, 0.12 * inch),
]

strength_table = Table(
    [
        [
            Paragraph("<b>Core Strengths</b>", styles["BodyText"]),
            Paragraph("<b>Technologies and Platforms</b>", styles["BodyText"]),
        ],
        [
            bullet_list(
                [
                    "Product design, strategic planning, architecture, development, and execution",
                    "Enterprise compliance, security, monitoring, and risk platforms",
                    "Team leadership, product strategy, and client-facing requirement translation",
                    "Startup ownership plus large-scale systems delivery",
                    "AI-forward learning mindset",
                ]
            ),
            bullet_list(
                [
                    "Python, Java, JavaScript, C, C++, Perl, HTML, DHTML, Shell Scripting",
                    "Ansible, Ajax, jQuery, UNIX",
                    "MySQL, Oracle, Aerospike",
                    "NoSQL, Relational Databases, Dashboards, Hybrid Mobile Apps",
                    "Machine Learning, AI Tools, Vibe Coding, Codex",
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

story += [Paragraph("Professional Experience", styles["SectionTitle"])]

experience_sections = [
    (
        "Stealth Mode Startup | Co-Founder | Apr 2023-Present",
        [
            "Focused on system architecture and product development.",
            "Worked across all product stages including end-to-end design, architecture, and development.",
            "Translated business requirements into technical solutions directly with clients.",
            "Designed and developed the complete tech stack including frontend, mid-tier, and database layers.",
            "Technologies: Python, HTML, JavaScript, MySQL.",
        ],
    ),
    (
        "PayPal, San Jose | Member of Technical Staff | Mar 2012-Mar 2023",
        [
            "Led compliance and security-related projects in the database team.",
            "Developed a monitoring platform for Aerospike across 2600+ servers and adjacent database systems.",
            "Evaluated roadmap, defined product strategies, designed features, led a team of 6+, and delivered against client requirements.",
            "Earlier built risk and fraud monitoring applications for 150+ services, plus web and hybrid mobile experiences for remote health and alert checks.",
            "Hosted technical expos and talks, joined hackathons, encouraged team participation, and won BeatCTF.",
            "Completed machine learning coursework and delivered introductory ML sessions internally.",
        ],
    ),
    (
        "PayPal, San Jose | Summer Intern - Software Engineer | Jun 2011-Nov 2011",
        [
            "Implemented Python-based monitoring modules interacting with MySQL data sources.",
            "Built one-pager application health views, alert dashboards, and a critical risk asset web application.",
            "Showcased dashboards during the university program and earned appreciation from Risk leaders.",
        ],
    ),
    (
        "Infosys, Pune | Senior Systems Engineer | Feb 2007-Feb 2010",
        [
            "Developed requirements in C++ using object-oriented programming.",
            "Handled black-box and white-box testing in UNIX.",
            "Automated test environments using shell scripting and Perl.",
            "Solved live issues while adhering to standard processes.",
        ],
    ),
    (
        "Cummins College of Engineering | Part-time Teaching Assistant | Jul 2006-Dec 2006",
        [
            "Six months of teaching assistantship experience at the beginning of the professional journey.",
        ],
    ),
]

for title, items in experience_sections:
    story.append(Paragraph(title, styles["RoleTitle"]))
    story.append(bullet_list(items))
    story.append(Spacer(1, 0.05 * inch))

story += [
    Paragraph("Education", styles["SectionTitle"]),
    bullet_list(
        [
            "M.S. in Computer Science, San Jose State University, CA | Dec 2011 | GPA 3.85",
            "B.E. in Computer Engineering, University of Pune, India | May 2006 | First Class with Distinction",
        ]
    ),
    Spacer(1, 0.05 * inch),
    Paragraph("Conference Paper and Publication", styles["SectionTitle"]),
    bullet_list(
        [
            "Presented at SVG Open 2011: “Drag and drop functionality for SVG using jQuery”.",
            "Published online in Journal in Computer Virology on April 3, 2012: “Opcode graph similarity and metamorphic detection”.",
        ]
    ),
    Spacer(1, 0.05 * inch),
    Paragraph("Awards", styles["SectionTitle"]),
    bullet_list(
        [
            "4 Spot Awards at Infosys for critical initiatives and projects successfully led and delivered.",
            "PayPal Blue Moon Award for successfully delivering Sandbox Risk in 2012 within a few months of joining.",
            "Infosys Bravo Award for developing a weekend support application using Perl and shell script within 3 days.",
        ]
    ),
]

doc.build(story)
print(PDF_PATH)
