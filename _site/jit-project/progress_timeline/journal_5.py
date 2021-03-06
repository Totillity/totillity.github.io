from _generate_site.elements import *

page = Page("jit-project/progress-timeline/journal-5.html",
            nav_loc=["JIT Project", "Progress Timeline", "[10] Journal 5"])

page += Title("Journal 5: Weeks 16-19")

page += Paragraph("March 21, 2021 - April 17, 2021")

page += Heading('Goals for this Journal:')
page += OrderedList([
    Paragraph("Implement Objects"),
    Paragraph("Implement Attribute Access and 'Setting'"),
    Paragraph("Research and Implement optimizations which can be done with Types"),
    Paragraph("Implement Nan-Boxing"),
    Paragraph("Implement Dynamic Type Checks"),
    Paragraph("Continue working on type-based optimizations"),
    Paragraph("Implement some form of Python Transpilation"),
    Paragraph("Ensure Python Compatibility"),
    Paragraph("Create and Run some tests"),
    Paragraph("Implement a Command Line Interface"),
    Paragraph("For further research, research what would be needed for JS or Lua transpilation"),
])

page += Heading("Research")

page += Paragraphs(f"""
{bold("Note: all references labelled at the bottom.")}
{bold("Note: I used code snippets instead of screenshots because this is a programming project.")}
{bold("Note: I used pseudocode instead of actual C for the sake of clarity.")}

The first two weeks of this time period were spent on making this JIT functional for everyday use. The most important step on that
journey is implementing objects, since a means of permanent, structured data storage is critical in programming. Although
the JIT could have technically made any calculation before, objects make it practical for everyday use.

This step requires an explanation of what exactly I mean by objects, though. In the strictest sense, objects are packets of
data which have a defined set of operations you can do on that data. Typically, this involves concepts such as methods, which
are functions which take the object as their first parameter implicitly. This is the model languages such as JavaScript and
Smalltalk (which essentially invented objects) follow. There are slightly more structured, if less powerful, models you can follow. 
Languages such as Java are near the extreme end of this, where objects must also be an instance of a class, which define exactly what
methods a given object can have, as opposed to Javascript where you can just add any old function to an object. Python strikes
a middle ground, where objects are created by classes and thus have a default set of methods, but where you can also extend
those objects with new methods and data at any time.

The objects I have implemented for ojit are even looser than in JavaScript. My objects are essentially just dictionaries/maps
which map names to objects. A function can be assigned to a name and be called that way like in the example: 
""")

page += Code("""
def fibo(n) {
    if (n < 2) {
        return n;
    } else {
        return fibo(n-1) + fibo(n-2);
    }
}

def main() {
    let holder = {};  // creates a new, empty object and assigns it to the variable `holder`
    holder.func = fibo;  // now, whenever we access holder.func, it gives us a reference to fibo
    return holder.func(20)  // returns 6765, the 20th fibonacci number
}
""")

page += Paragraphs(f"""
This behavior, however, doesn't implicitly pass the object as an argument to `fibo`. To have that behavior, you must instead use
the method call syntax, which uses a colon instead of a period for the attribute access:
""")

page += Code("""
def make_fraction(numerator, denominator) {
    let fraction = {};
    fraction.numerator = numerator;
    fraction.denominator = denominator;
    
    fraction.square_fraction = square_fraction;  // The important line
    return fraction;
}

def square_fraction(frac) {
    frac.numerator = frac.numerator * frac.numerator;
    frac.denominator = frac.denominator * frac.denominator;
}

def main() {
    let frac = make_fraction(2, 3);
    
    // this colon means the same thing as '.', except you also pass `frac` to the function as the first argument
    frac:square_fraction();
    return frac.numerator;  // returns 4
}
""")

page += Paragraphs(f"""
This is a much more general system than JavaScript's system and can therefore do anything JavaScript can do. The usage of
that will be clear when we get to transpilation.

Implementing objects was fairly straightforward. As I've mentioned before, underneath the hood, they are just dictionaries,
which I had already implemented earlier in order to support variables. Creating an object is just creating a dictionary,
and attribute access is just a hash_get operation. Setting an attribute isn't much harder, as long as you can set up the
parser so that it can tell the difference between an attribute access and an attribute set, which essentially comes down
to checking if there is an equals sign afterwards.

Now that I had working objects, I also had two different types of values. Before, there were only integers, but now there 
are objects and integers. These are fundamentally different types: you can only add and subtract integers, and you can only 
use attribute access and setting on objects. It doesn't have to be this way: you can make everything an object like Python
does, but this comes with a severe performance overhead since you have to do so many costly attribute access operations
even when you want to do something basic like addition. However, since I care quite a bit about performance (this being a 
JIT), I've elected to keep integers and objects separate. This brings up a new problem, though. Look at the following code:  
""")

page += Code("""
def foo(a) {
    let b = a + 3;
    let c = b * 3 - a;
    return c + 2;
}
""")

page += Paragraphs(f"""
What if some poor programmer tries calling this function, but passes an object as the argument? At this point, we must
warn the programmer that they have made an error, for nowhere in the function are objects used. And to do that, we have 
to set up code at the 'add' instruction to ensure that both of its arguments are in fact integers and not objects. And 
to do that, we somehow have to pass around the information about what type of value 'a' is just to be able to make the 
aforementioned check. Overall, this seems to add quite a bit of work that we have to do just before adding two values 
together. 

In fact, this work is the primary source of performance loss for many languages. In Python, every operation has at least 2
of those checks run on it, which quickly adds up. Java avoids most of this, but still must do frequent checks. Meanwhile,
a language like C or Rust does as few checks as possible when running. The only checks which do run are built into the hardware
at a fundamental level, and are therefore nearly free. My goal, therefore, is to avoid as many checks are possible.

The naive way of writing checks would be to emit a series of instructions to check that a value is of the proper type
every time we use it. This undoubtedly works, but it could be optimized quite a bit. For example, in the code sample above,
we know for a fact that both 'b' and 'c' are integers, and that 'a' is an integer after the first addition (because if it 
isn't, the function would have thrown the error and aborted the whole function by now). Therefore, the only check we actually
have to do is a single check on 'a' at the beginning of the function.

Now, how do we do a check? We could pass along an extra byte to store the tag with every value, but this very quickly doubles all memory usages,
which is something we want to avoid. After all, objects necessarily have to be 8 bytes (the size of a pointer on a 64-bit
system), and we can't just stuff an extra byte onto it. Registers themselves are 8 bytes, so keeping an object with a tag would
take 2 whole registers (one for the object, one for the tag), as opposed to just an object, which would just take one.
The solution is in realizing that pointers on a 64-bit system don't actually use all 64 bits, rather, they just use the first
48 bits, because you'd need a supercomputer to ever need the extra 16 bits of memory addressing space. Therefore, we can
use those first 16 bits for whatever we need, including storing the tag there. 

In reality, its a bit more complicated than that. The term used for this technique is called either NaN-boxing or NaN-tagging
by different people, because the technique has much more to do with the definition of the NaN (Not a Number) type by IEEE-754.
Essentially, the NaN type has 51 bits of extra space we can use. We use 3 of those for the tag, and the other 48 for the actual
data (48 bits for pointers, 32 bits for integers, and so on). These two optimizations (cutting unnecessary checks and 
folding tags into values) make type-checking as near to free as it can be without checking beforehand.

Now that we have types, the benefits of a JIT finally can come to the forefront. In a conventional interpreter like Python,
not a single type-check could have been eliminated. Meanwhile, in a compiler, we have no idea what type the argument is
and therefore couldn't use it as a valid program. The JIT lets us use the optimizations of a compiler while still accepting
programs it doesn't know everything about. 

Let's see the performance, then. We run the following code sections:
""")

page += Code("""
// ojit

def fibo(n) {
    if (n < 2) {
        return n;
    } else {
        return fibo(n-1) + fibo(n-2);
    }
}

def main(a1) {
    a1 = fibo(a1);
    return a1;
}
""")

page += Code("""
// python

def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


def main(a1):
    return fibo(a1)
""")

page += Paragraphs(f"""
When run, we find that the ojit code runs 90% faster than the python code (70 ms vs 7 ms), so I'd say my strategies work.

The final major step of my project is implementing transpilation. Transpilation is essentially just translating a file
from one programming language to another. The two code examples above are an example of transpilation. I (manually)
transpiled the ojit code into Python code. Both do the same thing (which is a requirement of transpilation), just in 
different languages. 

My goal was to create a program which automatically transformed Python code into ojit code, to make it easier to convert
existing programs in python into ojit to take advantage of the 90% performance improvement. Luckily, I had already done a 
similar task 3 years earlier when I wrote a Python-to-Java transpiler. I used many of the same techniques and strategies.
The most important of those is using Python's built-in reflection capabilities, where reflection is when a program can examine
its own code while its running. By using them, I can avoid a lot of work and let Python do the heavy lifting of parsing
for me. Once I have the parsed tree, I can simply examine each node of the tree individually and write the correct
ojit code into the output file. Just in case, here's the essential pseudo-code for such a tree-walk compiler:  
""")

page += Code("""
def emit_node(node) {
    switch (typeof node) {
        // call a different function depending on the type of the node
        // many of those functions will then recursively call this one again
        // for example, the function for an 'add' node would call 'emit_node' on each
        // of its arguments
    }
}
""")

page += Paragraphs("""
One of the most important things to consider when writing a transpiler is the degree to which different languages
can be reasonable translated to one another. This isn't like human languages, where all languages describe the same
reality with the same general logical structures underlying them all (since we all have the same brain). Computer Languages
all aim to describe different things with occasionally vastly different schemes of representation. If you ever want a 
painful example of that, contrast a Lisp Program with a Java program. Since I had known all along that transpilation
was a goal, however, I designed ojit to be compatible with Python as much as possible. The best to do so is to ensure
that my language is more general than Python, so that anything which exists in Python can be translated to ojit, just
with more boilerplate code that a human would be too lazy to write. 

All in all, it was a fairly simple endeavor and I now have a working transpiler.

Tests were similarly easy, since I had done a few before. Full, professional C-testing software is overkill for the scope
of my project, so I elected to instead create a library of programs I expect to work with the expected output, and
set up a python script which will automatically run ojit on each of those programs and ensure they have the correct
output. To do so, I had to implement a command-line interface for ojit, so the python script actually had a way to
connect to ojit programmatically. In any case, with these two tasks complete, I finished the programming section of 
my senior project and moved on to prepping for the presentation. 
""")

page += Heading("Main Accomplishments")
page += OrderedList([
    Paragraph("Implemented objects, attributes, and attribute checks"),
    Paragraph("Implemented values, nan-boxing, type checks, and type check optimization"),
    Paragraph("Implemented a python-to-ojit transpiler"),
    Paragraph("Implemented a testing program"),
    Paragraph("Implemented a command line interface"),
])

page += Heading("Reflection")
page += Paragraphs(f"""
The final work for the project was all done essentially on schedule, which is surprising given that the other sections of
work took more time and effort than expected. However, it isn't a bad thing, so I won't complain about it. The journal
was also supposed to be larger in scope, but then I realized that the things I would have written (an account of the more
abstract problems I had solved) wouldn't have been interesting and/or comprehensible without a certain familiarity with
the internal workings of ojit I have not provided in these journals in the interest of clarity. 

Now, its time to work on the presentation. I have hope this will go smoothly, since I know my project inside and out. 
Additionally, perhaps my time in Speech and Debate will give me an edge in public-ish speaking.
""")

page += Heading("Sources:")
page += OrderedList([
    Paragraph(f"{hyperlink('x64 Instruction Reference', 'https://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-instruction-set-reference-manual-325383.pdf')}"),
    Paragraph(f"{hyperlink('Reference on x64 encoding #1', 'https://pyokagan.name/blog/2019-09-20-x86encoding/')}"),
    Paragraph(f"{hyperlink('Reference on x64 encoding #2', 'http://ref.x86asm.net/geek64.html')}"),
    Paragraph(f"{hyperlink('Reference on x64 encoding #3', 'https://wiki.osdev.org/X86-64_Instruction_Encoding')}"),
    Paragraph(f"{hyperlink('Reference on LLVMLite', 'https://llvmlite.readthedocs.io/en/latest/user-guide/ir/index.html')}"),

    Paragraph(f"{hyperlink('Smalltalk', 'https://en.wikipedia.org/wiki/Smalltalk')}"),
    Paragraph(f"{hyperlink('JavaScript', 'https://en.wikipedia.org/wiki/JavaScript')}"),
    Paragraph(f"{hyperlink('Example NaN-boxing implementation', 'https://github.com/zuiderkwast/nanbox')}"),
    Paragraph(f"{hyperlink('Another Example NaN-boxing implementation', 'http://www.craftinginterpreters.com/optimization.html#nan-boxing')}"),
])

__pages__ = [page]
