from _generate_site.elements import *

page = Page("jit-project/progress-timeline/week-4.html", nav_loc=["JIT Project", "Progress Timeline", "[5] Week 4"])

page += Title("Progress: Week 4")

page += Paragraph("November 7, 2020 - November 13, 2020")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('Implement the previously designed IR into my assembler'),
    Paragraph('Test that IR'),
    Paragraph('Ensure I fully implement the IR'),
])


__pages__ = [page]
