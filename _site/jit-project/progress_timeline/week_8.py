from _generate_site.elements import *

page = Page("jit-project/progress-timeline/week-8.html", nav_loc=["JIT Project", "Progress Timeline", "[10] Week 8"])

page += Title("Progress: Week 8")

page += Paragraph("January 16, 2021 - January 23, 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('Research some optimization techniques, first non-JIT specific'),
    Paragraph('Whenever I find one I want to implement, do so'),
])


__pages__ = [page]
