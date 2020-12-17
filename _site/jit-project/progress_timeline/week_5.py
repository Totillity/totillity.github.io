from _generate_site.elements import *

page = Page("jit-project/progress-timeline/week-5.html", nav_loc=["JIT Project", "Progress Timeline", "[6] Week 5"])

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


__pages__ = [page]
