from _generate_site.elements import *

page = Page("jit-project/progress-timeline/week-13.html", nav_loc=["JIT Project", "Progress Timeline", "[15] Week 13"])

page += Title("Progress: Week 13")

page += Paragraph("February 21, 2021 - February 27. 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('Finish implementing first set of optimizations'),
    Paragraph('Write up a long Journal about all this work that I\'ve done'),
])


__pages__ = [page]
