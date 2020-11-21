from _generate_site.elements import *

page = Page("jit-project/progress-timeline/week-2.html", nav_loc=["JIT Project", "Progress Timeline", "[2] Week 2"])

page += Title("Progress: Week 2")

page += Paragraph("October 24, 2020 - October 30, 2020")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph('Read up on x86 Assembly (the one used in my computer)'),
    Paragraph('Create a basic Assembler based on the reading'),
])

page += Heading("Journal For This Week")
page += Paragraph(f"""
The initial learning took a lot more effort than expected because no one on the internet can be bothered to make any 
x86 or x64 tutorials for Windows. Everything has to be for linux, the superior operating system which 1.53% of systems use.
""")

page += Paragraph(f"""
Knowing that all these tutorials would be for Linux, I spent a week in Summer Break trying to get a working Linux install
on my laptop. After numerous attempts, I finally got Ubuntu 20 to work well. Having done so, I began following the tutorials
on how to write and compile assembly.
""")

page += Paragraph(f"""
Luckily for me, I already knew a lot about how to write assembly, because it is designed very similar to interpreter bytecode,
since that's what it is deep down. That made it easy for me to figure out how to write it. The hard part of generating it a form 
usable by the computer. After a lot of googling and following the sources listed at the bottom of this journal, I finally figure that out too
and have now built a working prototype assembler, with calling capabilities
""")

page += Paragraph("Sources:")
page += OrderedList([
    Paragraph(f"{hyperlink('x64 Instruction Reference', 'https://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-instruction-set-reference-manual-325383.pdf')}"),
    Paragraph(f"{hyperlink('https://pyokagan.name/blog/2019-09-20-x86encoding/')}"),
    Paragraph(f"{hyperlink('https://eli.thegreenplace.net/2013/11/05/how-to-jit-an-introduction')}"),
    Paragraph(f"{hyperlink('http://ref.x86asm.net/geek64.html')}"),
    Paragraph(f"{hyperlink('https://wiki.osdev.org/X86-64_Instruction_Encoding')}"),
    Paragraph(f"{hyperlink('https://stackoverflow.com/questions/15020621/what-is-between-esp-and-ebp')}")
])

__pages__ = [page]
