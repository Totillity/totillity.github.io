from _generate_site.elements import *

page = Page("jit-project/progress-timeline/week-7.html", nav_loc=["JIT Project", "Progress Timeline", "[8] Week 7"])

page += Title("Progress: Week 7")

page += Paragraph("January 9, 2021 - January 15, 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('Implement a way to generate the IR from the frontend'),
    Paragraph('Out of all the steps so far, this is the most likely to either fail or work poorly.'),
    Paragraph('Therefore, also use this week to implement all the improvements and fixes I’ve thought of over the past 7 weeks'),
])


__pages__ = [page]
