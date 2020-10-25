from _generate_site.elements import *

page = Page("jit-project/whats-a-jit.html", nav_loc=["JIT Project", "What's a JIT?"])


page += Title("What's a JIT?")

page += Paragraph("""
A JIT is a "Just in Time" compiler.
""")

page += Paragraph(f"""
Let's start by explaining how computers work. In the center of your computer is a CPU, a central processing unit.
This CPU is a intricate tangle of transistors and wires that all serve to execute the code stored on your computer.
The code that the CPU executes is called "Machine Code". It is a very different type of code than what people usually program in.
While normal programming languages like Python and Haskell are typically written and stored on the computer as text, 
machine code is stored entirely in raw bytes (although you can generate it using a textual medium). For example, 
here's a example of a program in machine code that would square a number in hex: 
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




__pages__ = [page]
