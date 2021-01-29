from _generate_site.elements import *

page = Page("jit-project/progress-timeline/week-9.html", nav_loc=["JIT Project", "Progress Timeline", "[11] Week 9"])

page += Title("Progress: Week 9")

page += Paragraph("January 24, 2021 - January 31, 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('Same as last week'),
    Paragraph('Look up some optimization techniques, this week preferably JIT specific'),
    Paragraph('Whenever I find one I want to implement, also do so'),
])


__pages__ = [page]
