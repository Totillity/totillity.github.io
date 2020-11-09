from _generate_site.elements import *

page = Page("jit-project/whats-a-jit.html", nav_loc=["JIT Project", "[1] What's a JIT?"])


page += Title("What's a JIT?")

page += Paragraph("""
A JIT is a "Just in Time" compiler.
""")

page += Paragraph(f"""
To fully understand what that means and why its useful, we first have to examine how computers work. 
""")

page += Paragraph(f"""
In the center of every computer is a processor. This processor can only do it's job if you provide it instructions in a 
very specific format, "machine code". This limitation exists for a variety of reasons, but to keep it simple, let's just
say that "machine code" is the best way to encode the reality of how processors physically work.
""")

page += Paragraph(f"""
If you're used to programming in anything other than assembly, the way machine code is structured will be alien to you.
It's all in raw bytes, it doesn't have variables, and to make and call functions, it's much more work than just {inline_code('print("hi")')}.
All these quirks and some more make writing programs in machine code (or assembly, which is machine code but not in bytes) very hard.
""")

page += Paragraph(f"""
The tradeoff here is that machine code programs are very fast. Simple programs like a fibonacci sequence calculator can be over
100x faster when written in machine code compared to Python. More complex programs, such a neural net for machine learning or
a n-body simulation are simply not feasible to run in anything but machine code since they need all the speed they can get.
""")

page += Code("""55 48 89 E5 89 7D FC 8B 45 FC 0F AF C0 5D C3""")

page += Paragraph("""
Luckily, we can output machine code without having to write each individual byte, using a tool called assembly.
Assembly's whole purpose is that a special tool called an assembler can convert it into machine code. 
Why do we need to go to all these lengths to make programs which can run on a CPU?
A CPU cannot run code in any other way than machine code for two reasons.
""")

page += Paragraph("""
First, the realities of computer hardware are much different than what Python, Java, Haskell, or even C will pretend.
One common trait those languages all share is that they pretend that we have infinite places to store things, and that 
all things are stored in the same place. While that is a useful way to reason about things since it makes writing programs
easier, machine code is the level in which we have to acknowledge that the above abstractions are just that, abstractions.  
""")

page += Paragraph(f"""
Python will pretend that you can have infinite variables and objects just 'exist'. In reality, computer have limited memory,
and that the object has to go {italics("somewhere")} in that memory, and we need to keep track of where that memory is.
In addition, modern computers have multiple levels of memory, each of which is progressively smaller in size but faster in speed 
than the last.
""")

page += Paragraph(f"""
Some further reading and bibliography:
""")

page += OrderedList([
    Paragraph(f"An online assembler to make machine code from assembly: {hyperlink('https://defuse.ca/online-x86-assembler.htm#disassembly')}"),
    Paragraph(f"Godbolt, an online C compiler that converts your C code into assembly. You can use it in conjunction "
              f"with the online assembler to see how some C code will convert into assembly: {hyperlink('https://godbolt.org/')}")
])


__pages__ = []
# __pages__ = [page]
