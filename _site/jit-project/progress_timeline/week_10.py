from _generate_site.elements import *

page = Page("jit-project/progress-timeline/week-10.html", nav_loc=["JIT Project", "Progress Timeline", "[12] Week 10"])

page += Title("Progress: Week 10")

page += Paragraph("January 31, 2021 - February 6. 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('In a change from the previous schedule, same as last week'),
    Paragraph('This is because I spent the last 2 weeks restructuring the compiler to make it easier to do optimizations'),
    Paragraph('Look up some optimization techniques, this week preferably JIT specific'),
    Paragraph('Whenever I find one I want to implement, also do so'),
])


__pages__ = [page]
