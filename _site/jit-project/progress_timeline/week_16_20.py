from _generate_site.elements import *

page = Page("jit-project/progress-timeline/week-16-20.html", nav_loc=["JIT Project", "Progress Timeline", "[9] Weeks 16 to 20"])

page += Title("Progress: Week 16")

page += Paragraph("March 21, 2021 - March 27, 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph("Implement Objects"),
    Paragraph("Implement Attribute Access and 'Setting'"),
    Paragraph("Research and Implement optimizations which can be done with Types"),
])

page += Title("Progress: Week 17")

page += Paragraph("March 28, 2021 - April 3, 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph("Implement Nan-Boxing"),
    Paragraph("Implement Dynamic Type Checks"),
    Paragraph("Implement some of those researched optimizations"),
])

page += Title("Progress: Week 18")

page += Paragraph("April 4, 2021 - April 10, 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph("Implement some form of Python Transpilation"),
    Paragraph("For further research, research what would be needed for JS or Lua transpilation"),
    Paragraph("Ensure Python Compatibility"),
])

page += Title("Progress: Week 19")

page += Paragraph("April 11, 2021 - April 17, 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph("Continue working on type-based optimizations"),
    Paragraph("Create and Run some tests"),
    Paragraph("Implement a Command Line Interface"),
])

page += Title("Progress: Week 20")

page += Paragraph("April 18, 2021 - April 24, 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph("Create a PowerPoint"),
    Paragraph("Write a Script"),
    Paragraph("Practice Presentation"),
])

__pages__ = [page]
