import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

pdf_path = r"c:\Users\Administrator\Desktop\Artificial-Intelligence-in-Software-Engineering\0. AI SQL to ORM Refactoring and Security Analysis\Nebyu_AI_SQL_to_ORM_Refactoring_and_Security_Analysis.pdf"
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=54,
    rightMargin=54,
    topMargin=54,
    bottomMargin=54
)

styles = getSampleStyleSheet()

# Custom Palette
PRIMARY_COLOR = colors.HexColor("#1A365D")   # Deep Navy
SECONDARY_COLOR = colors.HexColor("#2B6CB0") # Slate Blue
TEXT_DARK = colors.HexColor("#2D3748")       # Charcoal Body Text
BG_LIGHT = colors.HexColor("#F7FAFC")        # Light Gray Box
BORDER_COLOR = colors.HexColor("#E2E8F0")

title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=20,
    leading=24,
    textColor=PRIMARY_COLOR,
    spaceAfter=12
)

subtitle_style = ParagraphStyle(
    'DocSubtitle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    leading=14,
    textColor=SECONDARY_COLOR,
    spaceAfter=15
)

heading_style = ParagraphStyle(
    'SectionHeading',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=13,
    leading=16,
    textColor=PRIMARY_COLOR,
    spaceBefore=14,
    spaceAfter=8
)

body_style = ParagraphStyle(
    'BodyTextCustom',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    leading=14,
    textColor=TEXT_DARK,
    spaceAfter=10
)

code_style = ParagraphStyle(
    'CodeText',
    parent=styles['Normal'],
    fontName='Courier',
    fontSize=8.5,
    leading=11,
    textColor=colors.HexColor("#1A202C")
)

link_style = ParagraphStyle(
    'LinkText',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=14,
    textColor=colors.HexColor("#3182CE")
)

story = []

# Title & Metadata Header
story.append(Paragraph("Nebyu_AI: SQL to ORM Refactoring and Security Analysis", title_style))
story.append(Paragraph("<b>Learner:</b> Nebyu Assefa &nbsp;|&nbsp; <b>Course:</b> AI in Software Engineering &nbsp;|&nbsp; <b>Assignment:</b> W5 AI Lab", subtitle_style))
story.append(HRFlowable(width="100%", thickness=1.5, color=PRIMARY_COLOR, spaceAfter=15))

# 1. Prompt Formulation
story.append(Paragraph("1. Prompt Formulation", heading_style))
prompt_intro = (
    "Below is the exact text of the single, comprehensive prompt formulated for the AI assistant to "
    "refactor the procedural database script into a secure SQLAlchemy ORM version and analyze its security and professional benefits:"
)
story.append(Paragraph(prompt_intro, body_style))

prompt_text = """
<b>Act as a Senior Database Architect and Python Engineer. Refactor the following procedural MySQL database script into a modern, production-grade SQLAlchemy ORM implementation.</b><br/><br/>
<b>Initial Procedural Code:</b><br/>
<font name="Courier" size="8">
import mysql.connector<br/>
from mysql.connector import Error<br/><br/>
def get_connection():<br/>
&nbsp;&nbsp;&nbsp;&nbsp;return mysql.connector.connect(<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host="localhost", user="root", password="yourpassword", database="example_db"<br/>
&nbsp;&nbsp;&nbsp;&nbsp;)<br/><br/>
def create_user(db_cursor, username, email):<br/>
&nbsp;&nbsp;&nbsp;&nbsp;if not username or not email:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print("Username and email are required.")<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return<br/>
&nbsp;&nbsp;&nbsp;&nbsp;sql = "INSERT INTO users (username, email) VALUES (%s, %s)"<br/>
&nbsp;&nbsp;&nbsp;&nbsp;try:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;db_cursor.execute(sql, (username, email))<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(f"User '{username}' created successfully.")<br/>
&nbsp;&nbsp;&nbsp;&nbsp;except Error as e:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(f"Error creating user: {e}")<br/>
</font><br/>
<b>Requirements:</b><br/>
1. Define the User class as a SQLAlchemy declarative model containing columns for id (autoincrement primary key), username (unique string), email (unique string), and created_at (datetime).<br/>
2. Show how to create the database table (Base.metadata.create_all), instantiate an ORM engine and Session, add a new user object, query for that user, update their email, and delete the user using ORM methods.<br/>
3. Explain in detail why the SQLAlchemy (ORM) version is a significantly more professional, maintainable, and secure solution compared to procedural raw SQL string manipulation.
"""
story.append(Paragraph(prompt_text, code_style))
story.append(Spacer(1, 10))

# 2. Execution Screenshot
story.append(Paragraph("2. Execution Screenshot", heading_style))
screenshot_intro = (
    "The screenshot below captures the complete AI response, clearly illustrating the declarative User model definition, "
    "table creation, session-based CRUD workflow, and the detailed security analysis."
)
story.append(Paragraph(screenshot_intro, body_style))

img_path = r"c:\Users\Administrator\Desktop\Artificial-Intelligence-in-Software-Engineering\0. AI SQL to ORM Refactoring and Security Analysis\execution_screenshot.png"
if os.path.exists(img_path):
    img = Image(img_path, width=500, height=270)
    story.append(img)
story.append(Spacer(1, 12))

# 3. Verification and Reflection
story.append(Paragraph("3. Verification and Reflection", heading_style))

p1 = (
    "<b>Abstraction and Type Safety:</b> Transitioning from procedural SQL string manipulation to an Object-Relational "
    "Mapper (ORM) like SQLAlchemy fundamentally transforms how database entities and interactions are represented within software architecture. "
    "By abstracting relational database tables into native Python domain objects, ORM replaces raw SQL strings and unstructured tuple indices "
    "(e.g., <i>user[0]</i>, <i>user[1]</i>) with strongly-typed object attributes (<i>user.id</i>, <i>user.username</i>). This object-centric "
    "abstraction eliminates entire categories of runtime errors, such as syntax mistakes in SQL text or out-of-bounds array access when retrieving query columns. "
    "Furthermore, SQLAlchemy constructs query expressions through pythonic objects (<i>session.query(User).filter(User.username == username)</i>), "
    "enabling static type checkers, IDE auto-completion, and compile-time inspection to catch flaws early in the development lifecycle before any query reaches the database server."
)
story.append(Paragraph(p1, body_style))

p2 = (
    "<b>Maintainability and Architectural Resilience:</b> From a long-term maintainability perspective, an ORM model serves as a centralized single "
    "source of truth for the entire application schema. In procedural architectures, modifying a single column name or data type requires manually locating and "
    "updating every raw SQL string scattered across repository modules. In contrast, updating an ORM declarative model automatically reflects schema changes across all "
    "CRUD operations, query builders, and database migrations via tools like Alembic. Moreover, ORM abstracts away database dialect specifics, allowing an application to switch "
    "seamlessly between MySQL, PostgreSQL, or SQLite without rewriting a single line of business logic. This decoupling enhances code reusability, modularity, and testability, "
    "empowering engineering teams to maintain high code velocity and system reliability over complex software lifetimes."
)
story.append(Paragraph(p2, body_style))
story.append(Spacer(1, 10))

# 4. GitHub Repository Update
story.append(Paragraph("4. GitHub Repository Update", heading_style))
repo_intro = (
    "The initial procedural script, refactored SQLAlchemy ORM script, visual screenshot, and task README documentation have been "
    "committed and pushed directly to the dedicated task folder in the learner's GitHub repository:"
)
story.append(Paragraph(repo_intro, body_style))

repo_url = "https://github.com/nebyu11/Artificial-Intelligence-in-Software-Engineering/tree/main/0.%20AI%20SQL%20to%20ORM%20Refactoring%20and%20Security%20Analysis"
story.append(Paragraph(f'<b>Task Folder Link:</b> <a href="{repo_url}">{repo_url}</a>', link_style))
story.append(Spacer(1, 10))

files_summary = (
    "<b>Task Folder Content Checklist:</b><br/>"
    "• <b>procedural_user_manager.py</b>: Initial procedural MySQL connector script containing all CRUD functions.<br/>"
    "• <b>orm_user_manager.py</b>: Refactored SQLAlchemy ORM implementation with User declarative model, engine, session, and ORM CRUD operations.<br/>"
    "• <b>execution_screenshot.png</b>: Visual evidence capturing the complete prompt formulation and AI response.<br/>"
    "• <b>README.md</b>: Comprehensive task documentation detailing architecture, security benefits, and maintainability comparison."
)
story.append(Paragraph(files_summary, body_style))

doc.build(story)
print("PDF successfully generated at:", pdf_path)
