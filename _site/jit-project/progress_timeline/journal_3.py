from _generate_site.elements import *

page = Page("jit-project/progress-timeline/journal-3.html",
            nav_loc=["JIT Project", "Progress Timeline", "[16] Journal 3"])

page += Title("Journal 2: Weeks 8-13")

page += Paragraph("January 15, 2020 - February 27, 2021")

page += Heading('Goals for this Journal:')
page += OrderedList([
])

page += Heading("Research")

page += Paragraphs(f"""
{bold("Note: all references labelled at the bottom.")}
{bold("Note: I used code snippets instead of screenshots because this is a programming project.")}
{bold("Note: I used pseudocode instead of actual C for the sake of clarity.")}
""")

page += Heading("Reflection")
page += Paragraphs(f"""

""")

page += Heading("Main Accomplishments")
page += OrderedList([
])

page += Heading("Sources:")
page += OrderedList([
])

__pages__ = [page]
