from _generate_site.elements import *

page = Page("jit-project/progress-timeline/week-12.html", nav_loc=["JIT Project", "Progress Timeline", "[14] Week 12"])

page += Title("Progress: Week 12")

page += Paragraph("February 14, 2021 - February 20, 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('Still working on optimizations'),
    Paragraph('Primarily working on implementing the optimizations mentioned in the previous week'),
])


__pages__ = [page]
