from _generate_site.elements import *

page = Page("jit-project/whats-a-jit/chp-1.html", nav_loc=["JIT Project", "What's a JIT?", "[1] Chapter 1"])


page += Title("My JIT Project")

page += Paragraph("""
These pages outline my JIT Project and my progress on it. Additionally, they cover some of the context need to understand what a JIT is.
""")


__pages__ = [page]
