from _generate_site.elements import *

page = Page("jit-project/progress-timeline/journal-3.html",
            nav_loc=["JIT Project", "Progress Timeline", "[6] Journal 3"])

page += Title("Journal 3: Weeks 8-13")

page += Paragraph("January 15, 2020 - February 27, 2021")

page += Heading('Goals for this Journal:')
page += OrderedList([
    Paragraph('Research some non-JIT optimization techniques'),
    Paragraph('Research some JIT specific optimization techniques'),
    Paragraph('Whenever I find one I want to implement, do so'),
    Paragraph('Implemented include: Dead Code Elimination, Constant Folding, Instruction Emission Optimization'),
])

page += Heading("Research")

page += Paragraphs(f"""
{bold("Note: all references labelled at the bottom.")}
{bold("Note: I used code snippets instead of screenshots because this is a programming project.")}
{bold("Note: I used pseudocode instead of actual C for the sake of clarity.")}

Originally, this journal was to be primarily focused on my initial efforts to implement the parts of a JIT that make it a JIT.
However, there is an issue with that: those parts don't work until I do some preliminary work that makes it more of an AOT compiler
than a jit. Therefore, this journal will cover the AOT optimization techniques I've implemented, and the initial work to implement
the JIT part.

First, I'll explain the basic idea of code optimization. Say a programmer wrote this code:   
""")

page += Code("""
def foo() {
    a = 7 * 3
    b = a + 4
    c = b + a
    return c
}
""")

page += Paragraph(f"""
It is very easy for a human to see that all this work of addition and multiplication doesn't need to be done everytime
this code is run. The loads, multiplications, additions, and stores would create a lot of extra work that doesn't need to be
done. Rather, the following code would have the exact same end result, but would run significantly faster:
""")

page += Code("""
def foo() {
    return 46
}
""")

page += Paragraph(f"""
This change has removed 3 variables and 3 operations, making it an excellent {italics('optimization')}. As you've probably guessed,
an optimization is simply any change to a program which makes it have the same result, but use less of some valuable resource,
such as time, I/O, or memory. A compiler optimization is any routine within the compiler which attempts to optimize the code it
is given in some particular way. An optimization is a particular strategy to optimize code.
""")

page += Paragraph(f"""
The hard part of all this, of course, is getting a computer to understand a program well enough that it can make it better.
This can be an extremely challenging thing to do, if you do it naively. Take the following code: 
""")

page += Code("""
def bar() {
    x = 7 + 2
    y = x * 2 + x
    x = y - 3
    z = x * y - y
    return z + x
}
""")

page += Paragraph(f"""
Say you create an optimization where, whenever an arithmetic operation is applied to two constants and assigned to a variable (think 
{inline_code('a = 3 - 2')} or {inline_code('k = 55 / 5')}),
you replace all usages of that variable with the result of said arithmetic operation. You then apply that optimization to the above code once, 
getting:  
""")

page += Code("""
def bar() {
    // we know x = 7 + 2 = 9, so we remove the assignments to x and replace its usages with 9
    y = 9 * 2 + 9
    // this line (x = y - 3) can be removed, right???
    z = 9 * y - y
    return z + 9
}
""")

page += Paragraph(f"""
You might have seen the problem. Halfway through the function, we assign to x again, this time with a possibly different value.
Any usages of x after that point have to refer to a different value. We can't just naively replace variables whenever we want.
{italics('Or can we?')}
""")

page += Paragraph(f"""
SSA is a solution to this problem. It stands for Static Single Assignment form, but only the 'Single Assignment' part is what we care about.
In SSA form, all variables are assigned to only once. The function I've shown above would not be a valid SSA program, because
x is assigned to twice. However, it is fairly trivial to convert a non-SSA program to SSA form. Whenever you would assign to a variable
for the second time, like in the {inline_code('x = y - 3')} line, instead assign to a new variable and replace all future occurrences of the
original variable with the new one. For example, here's the previous function converted to SSA form:
""")

page += Code("""
def bar() {
    x = 7 + 2
    y = x * 2 + x
    x1 = y - 3
    z = x1 * y - y
    return z + x1
}
""")

page += Paragraph(f"""
As you can see, the x1's solve the problem of the same variable having different values in different parts of the program
Now, replacing variables with what we know is their constant value is much easier, especially for
the dumb computer. This shows just some of the value of SSA form. Now let's go over some optimizations. 
""")

page += Paragraph(f"""
{bold('Constant Folding')} is one of the simplest optimizations to understand, as it's the one I've been using as an example.
It's just replacing operations we know are on constants with their known result. Usually, multiple passes of this optimization are 
advisable. After just one iteration of {inline_code('bar')} from above (replacing x), it becomes:
""")

page += Code("""
def bar() {
    y = 9 * 2 + 9
    x1 = y - 3
    z = x1 * y - y
    return z + x1
}
""")

page += Paragraph(f"""
Knowing that more optimizations can be performed, we do a second iteration on the new code generated, replacing y, so it becomes: 
""")

page += Code("""
def bar() {
    x1 = 18 - 3
    z = x1 * 18 - 18
    return z + x1
}
""")

page += Paragraph(f"""
We can now replace x1, which makes our third iteration: 
""")

page += Code("""
def bar() {
    z = 15 * 18 - 18
    return z + 15
}
""")

page += Paragraph(f"""
Finally, on the 4th iterations, we've removed all variables and calculations: 
""")

page += Code("""
def bar() {
    return 267
}
""")

page += Paragraph(f"""
Constant folding has converted a function with lots of variables, operations, and general overhead into a near-zero cost function.
To actually execute this optimization, we just recognize whenever both arguments to an arithmetic operation are either constants, or
variables we know are constant.
""")

page += Paragraph(f"""
{bold('Dead Code Elimination (DCE)')} is an optimization which removes unused instructions. To see the usefulness of this,
I have to reveal that I've lied. Constant folding does not remove the assignments to variables we know are constant. It just 
replaces its usages, but not its definition, since that's not part of what it's supposed to do. Rather, Constant Folding defers
all useless-code removal to the DCE optimization.   
""")

page += Paragraph(f"""
DCE is a fairly simple optimization to understand; my previous definition just about sums it up. The primary way that this
pass detects what code is 'dead' is by seeing what variables are never accessed after they are assigned, which is obviously 
trivial to write as a computer program when the code to optimize is in SSA form. This would obviously be the case in the 
aftermath of the Constant Folding pass, when the variables have been turned into constants. In that case, then 
assignments can be removed.
""")

page += Paragraph(f"""
Unfortunately, removing dead code isn't quite as simple as destroying all unused variables. There is the possibility
that some code assigns some value to a variable, but that value was calculated in some way which has {bold('side effects')}.
Side effects are when some code has effects other than computing a value, like printing something to the screen or setting an
element of an array. In this case, removing code with side-effects just because its return value isn't used would fundamentally 
change the program, which isn't what we want to do. So a DCE pass would need to detect when some code has side effects and
only remove code which doesn't. This can be approximated by not just not removing function calls, which may or may not have side 
effects. 
""")

page += Paragraph(f"""
{bold('Instruction Emission Optimization (IEO)')} is my name for a practice which has many different names, mostly due to
how ubiquitous it is. The heart of this optimization is using the shortest/faster version of an Assembly instruction.
To see this in action, let's examine a case where we want to add the constant 45 to a variable which is currently stored in the
general purpose register RAX. The most obvious way to do so is with the following assembly: 
""")

page += Code("""
MOV RCX, 45
ADD RAX, RCX
""")

page += Paragraph(f"""
First, lets explain a bit about assembly. In x86 assembly, which is the instruction set most desktop computers use 
(as opposed to ARM, which is seen more in smart devices such as iPhones and microwaves), most instructions take two arguments. 
For instructions such as MOV, this makes sense. The line {inline_code('MOV RCX, 45')} {bold('mov')}es the constant 45 to RCX. 
In other words, the register RCX is set to 45. If the line was instead {inline_code('MOV RCX, RBX')}, then the value 
inside RBX is copied into RCX. We need a destination and a source, which fits into two arguments.
""")

page += Paragraph(f"""
However, the two=argument paradigm doesn't work so well when you come to instructions such as ADD. Here, you would think
you need 3 arguments, two for the actual things to add together and one to tell the computer where to put the result.
x86 gets around the problem by saying that the first argument is both one of the arguments, as well as the location to 
put the result. In simpler terms, the second argument is added into the first. Therefore {inline_code('ADD RAX, RCX')}
takes the values in RAX and RCX, adds them together, and stores the result in RAX.
""")

page += Paragraph(f"""
Together, these two instructions accomplish what we've set out 3 paragraphs ago. {inline_code('MOV RCX, 45')} puts 45 into 
RCX, which isn't currently used. Then, {inline_code('ADD RAX, RCX')} adds that 45 into RAX, our variable. We've added 45 to
our variable. However, it turns out that there is a shorter way to accomplish all of this.
""")

page += Paragraph(f"""
x86 provides for a form of ADD where the second argument is directly a constant. This makes the constant an {bold('immediate')}
because the cpu can immediately load that constant. In any case, if we use this new form of the ADD instruction, then we 
can eliminate the MOV entirely, cutting the instructions used in half, resulting in {inline_code('ADD RAX, 45')}. 
Additionally, we also cut the registers used to 0 new ones, saving RCX to be used elsewhere. Either effect would result 
in a speed-up, but combined, we see an even larger performance increase.
""")

page += Paragraph(f"""
This isn't all we can do in the field of IEO. But to see this next layer of it, we'll need to examine how assembly is encoded.
Somewhat obviously, computers don't run on text files. Opening up an executable in Notepad will show that, as Notepad will
give up on displaying the contents as actual text. Instead, computers take in raw bytes. The assembler's job is to transform
assembly code such as {inline_code('ADD RAX, RCX')} or {inline_code('MOV RCX, 45')} into bytes that the computer can understand.
I've written a simple assembler for my project, and we can examine it some more here.
""")

page += Paragraph(f"""
Intel is kind enough to provide a 2000+ page {hyperlink('manual', 'https://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-instruction-set-reference-manual-325383.pdf')}
on how x64 (the extension of x86 to 64-bit computers) is encoded.
Their first page on the MOV instruction (pg 687) provides a large table, which explains how each form of the MOV instruction,
such as the form with 2 registers as arguments, the form with 1 register and 1 memory location, the form with 1 memory
location and 1 constant, etc. are encoded. Let's look at a sample, which is the form with 
""")

page += Code(f"""
       Opcode       |    Instruction   |     |    Description
--------------------+------------------+ ... +--------------------
  REX.W+ B8 +rd io  |  MOV r64, imm64  |     | Move imm64 to r64
""")

page += Paragraph(f"""
Let's dissect the first two columns. The {bold('Instruction')} column tells us exactly what this
instruction is used for. The {inline_code('MOV')} tells us that this instruction is some type of MOV instruction, which 
copies data into other locations. The {inline_code('r64, imm64')} tells us the two arguments to the instruction, where 
{inline_code('r64')} is the first argument and {inline_code('imm64')} is the second. The {inline_code('r')} in {inline_code('r64')}
tells us that the first argument is a register, and the {inline_code('64')} tells us that it specifically assigns to the 
64 bit version of that register. The {inline_code('imm64')} tells us that the second argument is a {bold('64')} bit {bold('imm')}ediate.  
In total, this column tells us that this row refers to the form of the MOV instruction where it takes a 64 bit register 
and a 64 bit immediate. 
""")

page += Paragraph(f"""
The real meat is in the {bold('Opcode')} column, which tells you what bytes must be written to encode this form of the instruction. 
There are 4 distinct terms in {inline_code('REX.W+ B8 +rd io')}. {inline_code('REX.W+')} tells us that the encoding must
start with the REX byte. The REX byte is something new to x64, which serves the purpose of providing the extra data
needed to make this instruction 64-bit instead of 32-bit (I'll expend on this later). It takes the form {inline_code('0 1 0 0 w r x b')},
where {inline_code('0 1 0 0')} is a set sequence that marks this byte as a REX prefix, and {inline_code('w')}, 
{inline_code('r')}, {inline_code('x')}, and {inline_code('b')} are one bit flags. {inline_code('REX.W+')} 
means that the {inline_code('w')} bit should be set, which tells the CPU that this is a 64 bit version of an instruction 
that is normally 32 bit. {inline_code('B8 +rd')} are two 
separate terms which should be interpreted together. Normally, {inline_code('B8')} would provide the instruction code,
which is what tells the CPU what instruction these bytes are referring to. However, the extra {inline_code('+rd')} tells
us that the CPU can infer the instruction (MOV r64, imm64) just from the first 5 bits of the {inline_code('B8')} byte (which
is {inline_code('1 0 1 1 1 0 0 0')} in total),
and that we can therefore encode the register in the last 3 bits. RAX, for example, has the code, in bits, {inline_code('0 0 0 0')}.
R12 has the code, in bits, {inline_code('1 1 0 0')}. We take the last 3 bits and stick them onto the end of {inline_code('B8')}
to specify the register. The byte would therefore be just {inline_code('B8')} if the register is RAX, and {inline_code('BC = 1 0 1 1 1 1 0 0')}
if the register is R12. But what do we do with the first bit? After all, we need it to differentiate RAX and R8, which have the same
final 3 bits. We stick that one bit in the REX byte, which shows its purpose now. Finally, the {inline_code('io')} tells us
that we need to stick 8 bytes on the end to store the {bold('i')}mmediate. The {inline_code('o')} is what tells us we
need 8 bytes. Those 8 bytes will store the 64 bit constant used by this form of the MOV instruction.
""")

page += Paragraph(f"""
Let's try this out on {inline_code('MOV RCX, 45')}. The REX byte will just be {inline_code('0 1 0 0 1 0 0 0')}. The {inline_code('w')} must be
set as long as we are using this form, but the rest are not since there is no call to use them. The {inline_code('B8 +rd')} byte
actually becomes {inline_code('B8 + 01 = 1 0 1 1 1 0 0 1')}. And the constant bytes are, byte-wise, {inline_code('2d 00 00 00 00 00 00 00')}
since x86 and x64 is little-endian, where the lowest byte comes first. All together, that becomes {inline_code('48 B9 2d 00 00 00 00 00 00 00')}.
Checking with an online disassembler confirms that this is indeed how you encode {inline_code('MOV RCX, 45')} in bytes. 
""")

page += Paragraph(f"""
Returning to the final method of IEO I mentioned earlier, the secret to creating better assembly code lies in which form of 
an instruction you choose. If there is a form which is somehow shorter, then it's usually significantly better because it
saves time on the CPU decoding it, as well as the fact that shorter instructions means that more can be fit on one cache line.
In the case I've been talking about above, we can turn to an alternate, faster form for this instruction:  
""")

page += Code(f"""
       Opcode       |    Instruction   |     |    Description
--------------------+------------------+ ... +--------------------
     B8 +rd id      |  MOV r32, imm32  |     | Move imm32 to r32
""")

page += Paragraph(f"""
The major difference with this form is that it takes all 32 bit constants instead of 64 bit ones, it doesn't use a REX
byte, and it assigns to 32 bit registers. Each of those qualities is a benefit when compiling {inline_code('MOV RCX, 45')}.
Since our constant doesn't actually need all 8 bytes, saving 4 bytes on the instruction size by going down to a 4 byte constant
cuts down on the instruction size by nearly 1/2. The omission of the REX byte results from the instruction using 32 bit registers,
which saves us another byte. Finally, x64 specifies that when a 32 bit register is mov'ed to, the top 32 bits of that register
are zeroed, which means that using a 32 bit and a 64 register are effectively identical for us.  
""")

page += Paragraph(f"""
When encoding {inline_code('MOV RCX, 45')} according to this form instead of the previous form, the end result is 
{inline_code('B9 2d 00 00 00')}, which is half the size yet does the exact same task. Therefore, choosing an instruction
encoding form is one of the most impactful things which can be done when doing IEO.
""")

page += Paragraph(f"""
But all this theory is for naught if it doesn't produce concrete gains in performance. So let's examine 4 cases. One will
use my JIT without optimization, one will use my JIT with optimization, and the final one will use Python. All will have 
identical effects, but differing times.
""")

page += Paragraph(f"""
First case: my JIT without optimization. The code I handed the JIT was this:
""")

page += Code("""
def main(a1) {
    let a2 =  a1  + 3;
    let a3 =  a2  + 3;
    let a4 =  a3  + 3;
    let a5 =  a4  + 3;
    let a6 =  a5  + 3;
    let a7 =  a6  + 3;
    let a8 =  a7  + 3;
    let a9 =  a8  + 3;
    let a10 = a9  + 3;
    let a11 = a10 + 3;
    let a12 = a11 + 3;
    return    a12 + 3;
}
""")

page += Paragraph(f"""
Below is the generated assembly code, in the encoded and textual forms: 
""")

page += Code(f"""
5148baf01609000000000048b9401509000000000048b8b8184100000000004883ec20ffd04883c4204889c0594889c94883ec20ffd04883c4204889c048b903000000000000004801c848b903000000000000004801c848b903000000000000004801c848b903000000000000004801c848b903000000000000004801c848b903000000000000004801c848b903000000000000004801c848b903000000000000004801c848b903000000000000004801c848b903000000000000004801c848b903000000000000004801c8c3

mov rax,0x3
add rax,rcx
mov rcx,0x3
add rax,rcx
mov rcx,0x3
add rax,rcx
mov rcx,0x3
add rax,rcx
mov rcx,0x3
add rax,rcx
mov rcx,0x3
add rax,rcx
mov rcx,0x3
add rax,rcx
mov rcx,0x3
add rax,rcx
mov rcx,0x3
add rax,rcx
mov rcx,0x3
add rax,rcx
mov rcx,0x3
add rax,rcx
mov rcx,0x3
add rax,rcx
ret
""")

page += Paragraph(f"""
This is 205 bytes long. The code takes an average of 6 nanoseconds to execute. 
""")

page += Paragraph(f"""
When optimizations are turned on, the following assembly is generated: 
""")

page += Code(f"""
4889c80424c3

mov rax,rcx
add al,0x24
ret
""")

page += Paragraph(f"""
This is 6 bytes long. The code takes an average of 4 nanoseconds to execute. Although the code-size reduction is obviously 
impressive, the speed improvement doesn't look as impressive. In reality, that the code is probably even faster than it
appears because the overhead from the timing function. Additionally, many professional teams would sell their souls for
just a 10% improvement in their JIT speed-ups, sp a 33% improvement is very important. However, these numbers don't have any
meaning if this is actually 1000% slower than the alternatives to my JIT. So, let's look at the numbers for Python.
""")

page += Paragraph(f"""
I've written the following Python code, which does the exact same task the code for the JIT does:
""")

page += Code(f"""
def main(a1):
    a2 =   a1  + 3
    a3 =   a2  + 3
    a4 =   a3  + 3
    a5 =   a4  + 3
    a6 =   a5  + 3
    a7 =   a6  + 3
    a8 =   a7  + 3
    a9 =   a8  + 3
    a10 =  a9  + 3
    a11 =  a10 + 3
    a12 =  a11 + 3
    return a12 + 3
""")

page += Paragraph(f"""
This code takes an average of 1663 nanoseconds to execute a single iteration of the function. This means that my full 
JIT with optimizations is a 99.76% speed-up, or a 415.75x speed-up. All of these are excellent numbers, in my estimation,
so I'd say I'm doing pretty well.
""")

page += Heading("Reflection")
page += Paragraphs(f"""
Most of the work I did on the optimizations was done over the course of a week where I didn't have much to do for other
classes, except for 3 essays for AP Euro which I've since turned in. This gives me hope that I can fit work on my Senior
Project into my otherwise busy schedule.

This is definitely the most fun I've had writing a journal, which is why its so much longer than the previous ones,
and why it's slightly delayed. Even with all this text, I still haven't covered everything I wanted to. I'm working on an 
addendum like the {hyperlink('About', '/jit-project/about.html')} page, except covering the clever? way I've found to make
Dead Code Elimination come for free and Register Allocation significantly smarter (hint: go through the SSA-form IR backwards).

I'm not entirely sure what my future work on my project looks like. There's the obvious steps, like make the JIT usable
with support for loops, data types, and objects. Of course, once I implement those, I can get to the JIT parts of my JIT,
since support for those features was why JITs were invented. 

However, the hopes for Python integration look like a lot of extra work now that I've looked into parsing support more. 
The Python -> JIT step would be easy is there was any way to get Python parsing outside of Python. And if I have to lug 
the entire Python Binary and Standard Library just to get interop with it, what's the point? 

The really challenging parts of my project would be bringing it to a professional quality and giving it a Standard Library.
Both are some of the dullest things to do, but also the most important parts if you want public support for a programming
language implementation. It seems I won't do them though, because it would honestly be a pretty dumb to invest 3+ years of work
into a learning project. I don't want anyone to use this language. Already, I know things I'd do different if I was just
starting this project, like the choice of programming language.

So, my standard for the completion of this project is if I can make it again in itself, which is a fairly common standard 
for programming language projects. I believe this will be an achievable, if challenging, goal.

P.S. I added a usable mobile interface for this site if you want to check it out. Improvement coming there soon based on the
feedback of an unnamed student.
""")

page += Heading("Main Accomplishments")
page += OrderedList([
    Paragraphs("Added JIT wrapper"),
    Paragraphs("Instruction Selection Optimization"),
    Paragraphs("Added subtract and function calls"),
    Paragraphs("Added Constant Folding"),
    Paragraphs("Added memory management"),
    Paragraphs("Refactored code to facilitate further development"),
])

page += Heading("Sources:")
page += OrderedList([
    Paragraph(f"{hyperlink('x64 Instruction Reference', 'https://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-instruction-set-reference-manual-325383.pdf')}"),
    Paragraph(f"{hyperlink('Reference on x64 encoding #1', 'https://pyokagan.name/blog/2019-09-20-x86encoding/')}"),
    Paragraph(f"{hyperlink('Reference on x64 encoding #2', 'http://ref.x86asm.net/geek64.html')}"),
    Paragraph(f"{hyperlink('Reference on x64 encoding #3', 'https://wiki.osdev.org/X86-64_Instruction_Encoding')}"),
    Paragraph(f"{hyperlink('Wikipedia explaining the principles behind constant folding', 'https://en.wikipedia.org/wiki/Constant_folding')}"),
    Paragraph(f"{hyperlink('Wikipedia explaining the principles behind Dead Code Elimination', 'https://en.wikipedia.org/wiki/Dead_code_elimination')}"),
    Paragraph(f"{hyperlink('Wikipedia explaining the principles behind Instruction Emission', 'https://en.wikipedia.org/wiki/Instruction_selection')}"),
])

__pages__ = [page]
