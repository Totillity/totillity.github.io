from _generate_site.elements import *

page = Page("jit-project/progress-timeline/week-8-13.html", nav_loc=["JIT Project", "Progress Timeline", "[5] Weeks 8 to 13"])

page += Title("Progress: Week 8")

page += Paragraph("January 16, 2021 - January 23, 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('Research some optimization techniques, first non-JIT specific'),
    Paragraph('Whenever I find one I want to implement, do so'),
])

page += Title("Progress: Week 9")

page += Paragraph("January 24, 2021 - January 31, 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('Same as last week'),
    Paragraph('Look up some optimization techniques, this week preferably JIT specific'),
    Paragraph('Whenever I find one I want to implement, also do so'),
])

page += Title("Progress: Week 10")

page += Paragraph("January 31, 2021 - February 6. 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('In a change from the previous schedule, same as last week'),
    Paragraph('This is because I spent the last 2 weeks restructuring the compiler to make it easier to do optimizations'),
    Paragraph('Look up some optimization techniques, this week preferably JIT specific'),
    Paragraph('Whenever I find one I want to implement, also do so'),
])

page += Title("Progress: Week 11")

page += Paragraph("February 7, 2021 - February 13. 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('In a change from the schedule, still working on optimizations'),
    Paragraph('I\'ve done a lot of research on optimization techniques and discovered methods which apply to my project such as:'),
    Paragraph('Inline Caching, Dead Code Elimination, Constant Folding, Instruction Emission Optimization, Loop Invariant Code Motion'),
    Paragraph('The hard and time consuming part is, of course, implementing them, which is my goals'),
])

page += Title("Progress: Week 12")

page += Paragraph("February 14, 2021 - February 20, 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('Still working on optimizations'),
    Paragraph('Primarily working on implementing the optimizations mentioned in the previous week'),
])

page += Title("Progress: Week 13")

page += Paragraph("February 21, 2021 - February 27. 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('Finish implementing first set of optimizations'),
    Paragraph('Write up a long Journal about all this work that I\'ve done'),
])

__pages__ = [page]