from _generate_site.elements import *

page = Page("jit-project/progress-timeline/week-6.html", nav_loc=["JIT Project", "Progress Timeline", "[7] Week 6"])

page += Title("Progress: Week 6")

page += Paragraph("November 21, 2020 - November 28, 2020")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('Implement Parsing for the language'),
    Paragraph('Research better error handling and ast representation. Advisor could help a lot here.'),
    Paragraph('Learn how to do the above in C'),
])


__pages__ = [page]
