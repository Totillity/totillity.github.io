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
To actually execute this optimization, we just recognize whenever both arguments to an arithmetic operation 
""")

page += Paragraph(f"""
Constant folding has converted a function with lots of variables, operations, and general overhead into a near-zero cost function. 
""")

page += Heading("Reflection")
page += Paragraphs(f"""

""")

page += Heading("Main Accomplishments")
page += OrderedList([
])

page += Heading("Sources:")
page += OrderedList([
])

__pages__ = [page]
