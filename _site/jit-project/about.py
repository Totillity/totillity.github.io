from _generate_site.elements import *

page = Page("jit-project/about.html", nav_loc=["JIT Project", "[0] About"])


page += Title("My JIT Project")

page += Paragraph("""
These pages outline my JIT Project and my progress on it. Additionally, they cover some of the context need to understand what a JIT is.
""")

page += Heading("What Is My Project?")

page += Paragraph("""
My project will be a JIT (Just-in-Time) Compiler. A JIT is an technique to create faster interpreters, by compiling the 
interpreted code to machine code instead on the fly, which provides performance improvements in many cases, 
especially for code that is executed many times. It requires much more effort than either an interpreter or a compiler,
since it has to have both and the code to link them together, along with JIT specific code which provides its unique benefits.
""")

page += Heading("Goals")
page += OrderedList([
    Paragraph("Create a Terminal tool for Linux to run the JIT"),
    Paragraph("The JIT should have 2x the performance of the same code in Python"),
    Paragraph("The JIT’s transpiler from python should have 1.5x the performance of running it in CPython"),
    Paragraph("Transpiler should be able to run itself"),
    Paragraph("Stretch goal: 95% with CPython (there’s a lot of implementation details CPython exposes that preclude "
              "100% compatibility, any more than you can take a Steam Train and turn it into a Tesla Model 3)."),
])


page += Heading("Objectives")
page += OrderedList([
    Paragraph("Create a project to present to colleges"),
    Paragraph("Learn better Public Speaking"),
    Paragraph("Create a faster alternative with Python-ish sensibilities and syntax"),
    Paragraph("Learn Assembly coding and other low-level details of modern systems"),
    Paragraph("Learn how to focus on a single project for a long time")
])


page += Heading("Advisors")
page += OrderedList([
    Paragraph("Harish Kumar -- An expert advisors who can provide information on the practical side of my project, as well as feedback on all aspects of it."),
    Paragraph("Sendhil Palani -- A support advisor who'll help me stay on track."),
    Paragraph("Gajalakshmi Sendhil -- A support advisor who'll help me find the motivation to continue.")
])


page += Heading("Anticipated Research")
page += OrderedList([
    Paragraph("Optimization Techniques"),
    Paragraph("Prior JIT's"),
    Paragraph("Garbage Collection"),
    Paragraph("Assembly code"),
    Paragraph("Operating Systems"),
])


page += Heading("Technologies")
page += OrderedList([
    Paragraph("Linux -- Need to Learn"),
    Paragraph("Assembly -- Need to Learn"),
    Paragraph("IDE's such as Pycharm and CLion"),
    Paragraph("C Compilers such as GCC and Clang"),
    Paragraph("Programming Languages such as Python and C"),
    Paragraph("Libraries such as CFFI and Lark"),
])

__pages__ = [page]
