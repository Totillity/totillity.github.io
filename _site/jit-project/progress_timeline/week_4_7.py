from _generate_site.elements import *

page = Page("jit-project/progress-timeline/week-4-7.html", nav_loc=["JIT Project", "Progress Timeline", "[3] Weeks 4 to 7"])

page += Title("Progress: Week 4")

page += Paragraph("November 7, 2020 - November 13, 2020")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('Implement the previously designed IR into my assembler'),
    Paragraph('Test that IR'),
    Paragraph('Ensure I fully implement the IR'),
])

page += Title("Progress: Week 5")

page += Paragraph("November 14, 2020 - November 20, 2020")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('Look through current languages and see what I want mine to look like'),
    Paragraph('Based on my previous work, I can see what language design would lend itself best to JITing'),
    Paragraph('Design such a language'),
])

page += Heading("Thoughts")
page += Paragraphs(f"""
Looking at previous languages I used, and the work that I've don already, I think that my language needs a lot of 
flexibility. I want my language to be able to target multiple other languages (such as Python, Javascript, and Lua).
At the very least, I'll need very flexible hash-maps (dictionaries in python and objects in javascript) which can 
have multiple behaviors. After all, each language I listed above treats them differently. 

Beyond that, my default language will probably pull from python-style significant indentation. It looks much nicer,
especially because it wastes less space on '{{' and '}}'. I will need to see how python parses, it, though, because I don't
know for the life of me.
""")

page += Title("Progress: Week 6")

page += Paragraph("November 21, 2020 - November 28, 2020")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('Implement Parsing for the language'),
    Paragraph('Research better error handling and ast representation. Advisor could help a lot here.'),
    Paragraph('Learn how to do the above in C'),
])

page += Title("Progress: Week 7")

page += Paragraph("January 9, 2021 - January 15, 2021")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('Implement a way to generate the IR from the frontend'),
    Paragraph('Out of all the steps so far, this is the most likely to either fail or work poorly.'),
    Paragraph('Therefore, also use this week to implement all the improvements and fixes I’ve thought of over the past 7 weeks'),
])

__pages__ = [page]