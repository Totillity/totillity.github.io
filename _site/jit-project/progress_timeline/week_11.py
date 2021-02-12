from _generate_site.elements import *

page = Page("jit-project/progress-timeline/week-11.html", nav_loc=["JIT Project", "Progress Timeline", "[13] Week 11"])

page += Title("Progress: Week 11")

page += Paragraph("February 7, 2021 - February 13. 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('In a change from the schedule, still working on optimizations'),
    Paragraph('I\'ve done a lot of research on optimization techniques and discovered methods which apply to my project such as:'),
    Paragraph('Inline Caching, Dead Code Elimination, Constant Folding, Instruction Emission Optimization, Loop Invariant Code Motion'),
    Paragraph('The hard and time consuming part is, of course, implementing them, which is my goals'),
])


__pages__ = [page]
