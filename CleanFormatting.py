# Clean Code Chapter 5 – Formatting: Make Your Code Instantly Readable (with Python)
# clearly, flows smoothly, and earns respect in any code review."
# Unformatted code is like a novel with no paragraphs. Clean formatting enhances readability, communicates intent, and guides future developers.
#  It’s not just about aesthetics—it’s about professionalism.


# 1. VERTICAL FORMATTING
# Code should read like a story—main concepts come first, details follow.

class ReportGenerator:
    def __init__(self, db_connection):
        self.db = db_connection

    def generate_report(self):
        self._fetch_data()
        self._format_data()
        self._export_pdf()

    def _fetch_data(self):
        pass

    def _format_data(self):
        pass

    def _export_pdf(self):
        pass

# 2. Use Blank Lines to Separate Concepts
#Good Way
username = "jaeson"

print(f"Welcome, {username}")

#Bad Way
username = "jaeson"
# Avoiding blank lines can make code look cluttered and hard to read. Use blank lines to separate logical sections of your code.

print(f"Welcome, {username}")


# 3. HORIZONTAL FORMATTING
#Good way
price = 100
tax = 0.18
total = price * (1 + tax)

#Bad Way
price=100
tax=0.18
total=price*(1+tax)

#4. INDENTATION & NESTING
#Bad Way
if user:
    if user.is_logged_in:
        if user.can_edit:
            edit_document()

#Good Way
def can_edit(user):
    return user and user.is_logged_in and user.can_edit

if can_edit(user):
    edit_document()

# 5. TEAM FORMATTING STANDARDS
# javascript_code - eslint, .NET - Resharper, SonarLint, Java - Checkstyle, Python - Pylint, Black, Flake8, etc.
# 6. USE A LINTER

# Let’s recap:

# Format your code top-to-bottom and side-to-side.

# Use whitespace as punctuation.

# Avoid deep nesting.

# Respect team-wide conventions.

# So That your life can be better!!!!!


