from _generate_site.elements import *

page = Page("jit-project/progress-timeline/week-14-15.html", nav_loc=["JIT Project", "Progress Timeline", "[7] Weeks 14 to 15"])

page += Title("Progress: Week 14")

page += Paragraph("February 28, 2021 - March 6, 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('Finish implementing first set of optimizations'),
    Paragraph('Get those optimizations to actually work'),
    Paragraph('Implement a way to disable said optimizations, and ensure the program works with and without optimizations'),
    Paragraph('Write up a long Journal about all this work that I\'ve done'),
])


__pages__ = [page]
