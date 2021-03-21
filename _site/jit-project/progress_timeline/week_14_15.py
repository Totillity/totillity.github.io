from _generate_site.elements import *

page = Page("jit-project/progress-timeline/week-14-15.html", nav_loc=["JIT Project", "Progress Timeline", "[7] Weeks 14 to 15"])

page += Title("Progress: Week 14")

page += Paragraph("February 28, 2021 - March 6, 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph("Make Parameters and Branches work"),
    Paragraph("Generate said Parameters and Branches"),
    Paragraph("Implement If-statements"),
    Paragraph("Implement Comparisons"),
])

page += Title("Progress: Week 15")

page += Paragraph("March 7, 2021 - March 20, 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph("Implement Blocks"),
    Paragraph("Implement While-statements"),
    Paragraph(f"Create Instruction Emission Optimizations for everything implemented over these two weeks, like {inline_code('xor rax, rax')} over {inline_code('mov rax, 0')}"),
])


__pages__ = [page]
