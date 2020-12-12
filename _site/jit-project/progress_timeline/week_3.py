from _generate_site.elements import *

page = Page("jit-project/progress-timeline/week-3.html", nav_loc=["JIT Project", "Progress Timeline", "[3] Week 3"])

page += Title("Progress: Week 3")

page += Paragraph("October 31, 2020 - November 6, 2020")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('Read up on IR designs'),
    Paragraph('Look into what my IR will need'),
    Paragraph('Design an IR to fulfill those needs'),
])

__pages__ = [page]
