from _generate_site.elements import *

page = Page("jit-project/whats-a-jit/intro.html", nav_loc=["JIT Project", "What's a JIT?", "[0] Introduction"])

page += Title("What's A JIT?")

page += Paragraph("""
Simply put, a JIT is a Just In Time compiler. These next few pages will explain what each of those words mean.
""")


__pages__ = [page]
