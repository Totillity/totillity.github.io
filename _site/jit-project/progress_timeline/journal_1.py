from _generate_site.elements import *

page = Page("jit-project/progress-timeline/journal-1.html", nav_loc=["JIT Project", "Progress Timeline", "[2] Journal 1"])

page += Title("Journal 1: Weeks 1-3")

page += Paragraph("October 17, 2020 - November 6, 2020")

page += Heading("Research")

page += Paragraphs(f"""
{bold("Note: all references labelled at the bottom.")}

Over these 3 weeks, I've set out the basis of my project.

My plan for the project is to make a JIT.  So, over the first week, I conducted research on exactly what a JIT entails.
I had a pretty good idea beforehand, and my research confirmed what I knew, but also highlighted some more things I needed
to do. I already knew I would need to learn Assembly, design some good IR, and research and implement optimization techniques.
I learned from my research that there were in fact multiple ways to structure a JIT. To explain this knowledge, I'll explain 
at bit more of what a JIT is first:

A JIT is a 'Just In Time' compiler. Instead of turning a program into machine code ahead of time like an AOT compiler, or
running it without ever turning it into machine code like an Interpreter, a JIT turns it into machine code as it goes. This makes
JIT's a hybrid of the two other options. Making one, I knew, would take effort, but would combine the best aspects of compilers
and interpreters with few of their weaknesses. I learned that there are two schools of thought on how to generate that 
machine code (assembly) on the spot.

A 'Method JIT' is one option. This the path that many major JIT's such as V8 (Google), Hotspot (Oracle), and the CLR 
(Microsoft) use. In this path, every time we come to a new method, we compile the whole thing on the spot using 
information we've gathered over the program execution. This is a very simple way of JIT'ing, and judging by the big 
names involved, very effective.

A 'Tracing JIT' is another option. This is the path that LuaJIT takes. As I've mentioned before, as good as other JIT's are,
LuaJIT blows them out of the water. It runs Lua, a language that should be very slow due to its extremely dynamic nature.
Instead, LuaJIT speeds it up to the point where it can go toe-to-toe with C on some benchmarks. It does this by using a novel
means of JIT'ing: whenever it detects some code path that is executed repeatedly, like a hot loop or a highly recursive function,
compile the path that it taken inside of that loop, collapsing inner loops, conditionals, and jumps. By doing so, the regions
of code which cause the most slow-downs are the most heavily optimized. However, this is an exceedingly difficult thing to code.

In light of that, I think I'll be taking the relatively easy approach of writing a Method JIT. Although there is one Tracing
JIT success story, it seems that Method JIT's are much more consistently good. Additionally, as this is my first time writing a JIT,
it's advisable that I don't go in over my head.

Luckily, I don't have to make a decision on that yet, since I won't need it until next semester, when I implement the JIT parts of my JIT. 
For now, I am working on the things I know I'll need, no matter what path I choose. This includes the assembler, the IR, and the parser.

The assembler is likely the newest area that I will learn in this whole endeavor. Assembly is very alien to me, who uses mostly
Python. In learning it, however, I had the distinct advantage that I had used and worked on various IR's before, in my other programming
languages. Assembly is essentially an IR for the CPU, so it shares many structural similarities. For example, they both get
rid of variables entirely, which are just an abstraction. They make constants and each of the steps of expressions explicit, to better
represent what is going on in the background. This all made following tutorials on the nuts and bolts of how x64 assembly 
(the variant my computer uses) much easier.

Even if I had a general grasp of how assembly worked, I still needed to be able to generate it, since I'm not the one 
compiling function on the fly, my computer is.  This was actually more difficult than expected, for two reasons. First,
x64 assembly is encoded very differently than it's text form would suggest, mostly to be able to shove as much information 
into as little of a space as possible. This is a fairly reasonable thing for Intel to do, as they needed to squeeze every drop
of performance out of silicon and this compactification scheme helps with that. Second, and more importantly, the lack of 
easily locatable tutorials that explain how to encode x64 assembly made it difficult to learn it. This is also reasonable,
since this is not a very common use case. Assemblers exist to do this for you, but unfortunately, an external assembler
cannot be used in my project. It would be too slow. Luckily, I found materials eventually, which helped me understand how
x64 is encoded. This full explanation will take an entire article (naturally), and the code is too long and complicated to reasonably
copy and explain here, so I'll just do a high level explanation of how the assembler I implemented works. But first, I'll 
need to explain how my IR works.

IR stands for 'Intermediate Representation'. It exists so that computers have a form that is easy for them to understand
and manipulate. There are three main levels of representation: Source code, IR, and Bytecode/Machine Code. Each ash its benefits, drawbacks, and uses.
Here's an example fo the same code in each of the formats (in order, source code, ir, bytecode) (in a made up language to better show what I'm doing):
""")

page += Code("""
def fibo(n: int) -> int {
    if (n < 2) {
        return n;
    } else {
        return fibo(n-1) + fibo(n-2);
    }
}
""")


page += Code("""
def fibo(n: int) -> int {
    tmp1: int = n
    tmp2: int = 2
    tmp3: bool = n < 2
    if (tmp3) {
        tmp4: int = n 
        return tmp4
    } else {
        tmp5 = n
        tmp6 = 1
        tmp7 = tmp5-tmp6
        tmp8 = fibo(tmp7)
        tmp9 = n
        tmp10 = 2
        tmp11 = tmp9-tmp10
        tmp12 = fibo(tmp11)
        tmp13 = tmp8 + tmp12
        return tmp13
    }
}
""")


page += Code("""
FUNCTION(name="fibo", args=["n": int32], ret=int32) 
{
    0  LOAD_VAR("n")
    1  LOAD_CONST(2)
    2  LESS_THAN()
    3  JMP_IF_FALSE(6)
    4  LOAD_VAR("n")
    5  RETURN()
    6  START_ARGS()
    7  LOAD_VAR("n")
    8  LOAD_CONST(1)
    9  SUBTRACT()
    10 FINISH_ARGS()
    11 LOAD_VAR("fibo")
    12 CALL()
    13 START_ARGS()
    14 LOAD_VAR("n")
    15 LOAD_CONST(2)
    16 SUBTRACT()
    17 FINISH_ARGS()
    18 LOAD_VAR("fibo")
    19 CALL()
    20 ADD()
    14 RETURN()
}
""")

page += Paragraphs(f"""
As you can see, Source code is the most readable to humans, as well as the least redundant. IR is more redundant,
but in such a way that all relationships between all quantities are made clear. Bytecode is very redundant and near impossible 
for a human to interpret, but makes it very clear what steps to execute and in what order. These qualities determine how each is used.
Source code is used by humans wherever they can. It is the one that is most often programmed in. IR is used whenever a 
computer wants to examine what a program does, how it does it, and how to make it do the same thing, but faster. And finally, either bytecode or machine
code, which makes the steps explicit, is used whenever the code is actually run. Each of these formats can be converted to the others
very cleanly, although the typical flow is source -> IR -> bytecode/machine code.

Back to IR. As I've mentioned, IR is special because it is the place where all relationships become clear. Converting between equivalent
IR's should be as trivial as rewriting {inline_code('a+b')} as {inline_code('b+a')}, or factoring {inline_code('xt + yt')} into 
{inline_code('t(x + y)')}. Be being able to easily convert between such functionally equivalent forms, we can try finding the best way of
doing what is in the program. If we calculate one expensive value in a spot and can reuse it in another without having to calculate
it again, we should be able to rewrite the code so it isn't recalculated. This is only one among the many possible optimizations we can do.

Critical to all this is a good IR design. With a mediocre or naive design, we could find ourselves in a situation where some 
fact is blindingly obvious to a human, but the limitations of the IR prevent the computer from seeing it. Without a thoughtful
IR design, all the work put into a JIT is for naught. Therefore, I spent a lot of time going over what other, smarter people 
designed their IR as. I'll list some of the things I learned from some of the places I searched:  
""")

page += OrderedList([
    Paragraph("""From LLVM IR, I learned of SSA form. This is a form in which each variable is only assigned to once, which 
    makes reasoning about variable lifetimes and their contents much simpler. This is an excellent addition."""),
    Paragraph("""From Python Bytecode, I learned how, if you make the IR serializable, it can be redistributed to make
    product distribution so much easier and faster."""),
    Paragraph("""From the Crafting Interpreters IR, I of course learned what an IR is, as well as some critical facts about them.""")
])

page += Paragraphs(f"""
With all these lessons in mind, here are the basics of my IR design for this project:
""")

page += OrderedList([
    Paragraph("""Each program is split into functions, which fit the Method-JIT idea very well."""),
    Paragraph("""Each function is split into blocks. Each block is a place where no flow in or out occurs within. This
    makes reasoning about them very easy"""),
    Paragraph("""Inside each block is a list of statements, each of which assign their return value to a name, Other statements
    can use those names as arguments. Each name is unique to a statement, to fulfill SSA."""),
    Paragraph("""There are many different statement types, such as Add, Load Constant, Parameter, and more to come."""),
    Paragraph("""At the end of each block is a single terminator, which controls what happens at the end of that block. Variants of terminators
    include returns, unconditional branches, and switches."""),
    Paragraph("""As a bonus, each statement assigning to one value makes that part of register allocation (next journal) much easier.""")
])

page += Paragraphs(f"""
Now that you understand the IR of my JIT, understanding how its assembler works should be a piece of cake. The assembler works by iterating
through each function and emits the assembly for that function. In each function, it iterates through each block and emits the appropriate
assembly for that block. The most novel part of my JIT is that, inside each block, it iterates through each statement in that block backwards.
The full potential of that will be explained in the next journal, but for now, let's just say that it allows us to exploit SSA much more.
It does, however, complicate code emission, since as I generate code, I have to do so backwards. Still, for each statement in that block,
the assembler emits the equivalent assembly (like the x64 add instruction for all adds), and the equivalent code for each terminator 
(like a x64 jmp for jumps). Thus, the code for the whole program can be generated. This is not yet a JIT, since none of this happens Just In Time.
That, too, shall be for later. 
""")

page += Heading("Reflection")
page += Paragraphs(f"""
Luckily, I had managed to cover a lot of this ground in my preparatory work over Summer Break. Most of it is still new,
aside from the preliminary research on x64 assembly. I have researched JIT types and decided on one (week 1), I've created an
assembler (week 2), and an IR (week 3). All of this code can be found on my Github. The Assembler mostly lives in 
{inline_code('(main.c) compiled_function')}. The IR is the various structs supporting it, such as {inline_code('struct BranchIR')}. 
I am slightly behind on the work for the next Journal, but only by a week, which is great because it gives me stuff to do over break.
Additionally, I've actually done week 4 in this journal as well, because implementing the IR I designed in week 3 is the only
way to make sure it works. 
""")

page += Heading("Main Accomplishments")
page += OrderedList([
    Paragraph("Completed Assembler (for now, I might need to improve it later)"),
    Paragraph("Completed IR (should be near its final state)"),
])

page += Heading("Sources:")
page += OrderedList([
    Paragraph(f"{hyperlink('What LuaJIT Does', 'http://lua-users.org/lists/lua-l/2010-03/msg00305.html')}"),
    Paragraph(f"{hyperlink('LuaJITs relative performance', 'https://wren.io/performance.html')}"),
    Paragraph(f"{hyperlink('An overview of PyPy, tracing JITs, and meta-tracing JITs', 'http://antocuni.eu/download/antocuni-phd-thesis.pdf')}"),
    Paragraph(f"{hyperlink('Whether to use a tracing or method jit', 'https://news.ycombinator.com/item?id=16204373')}"),
    Paragraph(f"{hyperlink('x64 Instruction Reference', 'https://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-instruction-set-reference-manual-325383.pdf')}"),
    Paragraph(f"{hyperlink('The best tutorial on x64 encoding', 'https://pyokagan.name/blog/2019-09-20-x86encoding/')}"),
    Paragraph(f"{hyperlink('A tutorial of the (boring) memory aspect of executable memory', 'https://eli.thegreenplace.net/2013/11/05/how-to-jit-an-introduction')}"),
    Paragraph(f"{hyperlink('Reference on x64 #1', 'http://ref.x86asm.net/geek64.html')}"),
    Paragraph(f"{hyperlink('Reference on x64 #2', 'https://wiki.osdev.org/X86-64_Instruction_Encoding')}"),
    Paragraph(f"{hyperlink('2198 page Reference on x64', 'https://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-instruction-set-reference-manual-325383.pdf')}"),
    Paragraph(f"{hyperlink('LLVM IR design', 'https://llvmlite.readthedocs.io/en/latest/')}"),
    Paragraph(f"{hyperlink('Crafting Interpreters IR Design', 'http://www.craftinginterpreters.com/contents.html')}"),
    Paragraph(f"{hyperlink('Python Bytecode/IR Design', 'https://docs.python.org/3/library/dis.html')}"),
])

__pages__ = [page]
