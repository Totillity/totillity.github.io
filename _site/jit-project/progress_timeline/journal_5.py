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
    Paragraph("Implement some of those researched optimizations"),
    Paragraph("Implement some form of Python Transpilation"),
    Paragraph("Ensure Python Compatibility"),
    Paragraph("For further research, research what would be needed for JS or Lua transpilation"),
    Paragraph("Continue working on type-based optimizations"),
    Paragraph("Create and Run some tests"),
    Paragraph("Implement a Command Line Interface"),
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
which I had already implemented earlier in order to support variables.
""")

page += Heading("Main Accomplishments")
page += OrderedList([

])

page += Heading("Reflection")
page += Paragraphs(f"""

""")

page += Heading("Sources:")
page += OrderedList([
    Paragraph(f"{hyperlink('x64 Instruction Reference', 'https://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-instruction-set-reference-manual-325383.pdf')}"),
    Paragraph(f"{hyperlink('Reference on x64 encoding #1', 'https://pyokagan.name/blog/2019-09-20-x86encoding/')}"),
    Paragraph(f"{hyperlink('Reference on x64 encoding #2', 'http://ref.x86asm.net/geek64.html')}"),
    Paragraph(f"{hyperlink('Reference on x64 encoding #3', 'https://wiki.osdev.org/X86-64_Instruction_Encoding')}"),
    Paragraph(f"{hyperlink('Reference on LLVMLite'), 'https://llvmlite.readthedocs.io/en/latest/user-guide/ir/index.html'}"),
    Paragraph(f"{hyperlink('Ternary Operator in JavaScript, and similar in C, Java C#, etc.'), 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator'}"),
    Paragraph(f"{hyperlink('Ternary Operator in Python'), 'https://docs.python.org/3/reference/expressions.html?highlight=ternary#conditional-expressions'}"),
    Paragraph(f"{hyperlink('Dominance Frontiers', 'https://en.wikipedia.org/wiki/Static_single_assignment_form#Computing_minimal_SSA_using_dominance_frontiers')}"),
    Paragraph(f"{hyperlink('Explanation of Overflow vs Carry Flag', 'http://teaching.idallen.com/dat2343/10f/notes/040_overflow.txt')}"),

])

__pages__ = [page]
