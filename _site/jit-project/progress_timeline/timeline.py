from _generate_site.elements import *

page = Page("jit-project/progress-timeline/timeline.html", nav_loc=["JIT Project", "Progress Timeline", "[0] Timeline"])

page += Title("Timeline for Project")

page += Heading('Week 1: Initial Design')
page += OrderedList([
    Paragraph('Look up previous work on JIT’s and how they work'),
    Paragraph('Based on that work, create a plan for how my JIT will work'),
])
page += Heading('Week 2: Prototype Assembler')
page += OrderedList([
    Paragraph('Read up on x86 Assembly (the one used in my computer)'),
    Paragraph('Create a basic Assembler based on the reading'),
])
page += Heading('Week 3: IR Design')
page += OrderedList([
    Paragraph('Read up on IR designs'),
    Paragraph('Look into what my IR will need'),
    Paragraph('Design an IR to fulfill those needs'),
])
page += Heading('Week 4: Implement IR')
page += OrderedList([
    Paragraph('Implement the previous IR into my assembler'),
    Paragraph('Test that IR'),
    Paragraph('Ensure I fully implement the IR'),
])
page += Heading('Week 5: Design Frontend')
page += OrderedList([
    Paragraph('Look through current languages and see what I want mine to look like'),
    Paragraph('Based on my previous work, I can see what language design would lend itself best to JITing'),
    Paragraph('Design such a language'),
])
page += Heading('Week 6: Implement Frontend')
page += OrderedList([
    Paragraph('Implement Parsing for the language'),
    Paragraph('Research better error handling and ast representation. Advisor could help a lot here.'),
    Paragraph('Learn how to do the above in C'),
])
page += Heading('Week 7: Hook up Frontend and Backend, General improvements #1')
page += OrderedList([
    Paragraph('Implement a way to generate the IR from the frontend'),
    Paragraph('Out of all the steps so far, this is the most likely to either fail or work poorly.'),
    Paragraph('Therefore, also use this week to implement all the improvements and fixes I’ve thought of over the past 7 weeks'),
])
page += Heading('Week 8: Optimization Techniques, Part 1')
page += OrderedList([
    Paragraph('Look up some optimization techniques, first non-JIT specific'),
    Paragraph('Whenever I find one I want to implement, do so'),
])
page += Heading('Week 9: Optimization Techniques, Part 2')
page += OrderedList([
    Paragraph('Look up some optimization techniques, this week preferably JIT specific'),
    Paragraph('Whenever I find one I want to implement, also do so'),
])
page += Heading('Week 10: Python Transpiler')
page += OrderedList([
    Paragraph('Find a way to transpile Python to my JIT'),
    Paragraph('Possibly use the ‘ast’ python module'),
])
page += Heading('Week 11: Profile Guided Optimization')
page += OrderedList([
    Paragraph('Run programs on my JIT, see where the biggest slowdowns are'),
    Paragraph('Slow downs in the JIT itself can be optimized'),
    Paragraph('Slow downs from the JIT not optimizing can also be corrected by researching and implementing more optimizations'),
])
page += Heading('Week 12: General Improvements #2')
page += OrderedList([
    Paragraph('Implement the other ideas that came to me during the past 12 weeks'),
    Paragraph('For example, I think I’ll add support for Windows here, which will likely just mean adding another calling convention'),
])
page += Heading('Week 13: Professional-ize project')
page += OrderedList([
    Paragraph('Clean-up code'),
    Paragraph('Write tests'),
    Paragraph('In my site, write documentation on how the JIT works, and how to use it'),
])
page += Heading('Week 14: Final Week')
page += OrderedList([
    Paragraph('This week might be a result of my miscount. In which case, shift this workload a week earlier'),
    Paragraph('Otherwise, prep for my final project presentation.'),
    Paragraph('Also, a flex week for the work that might be postponed due to Tests and other sources of stress'),
])


__pages__ = [page]
