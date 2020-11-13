from _generate_site.elements import *

page = Page("jit-project/progress-timeline/week-1.html", nav_loc=["JIT Project", "Progress Timeline", "[1] Week 1"])

page += Title("Progress: Week 1")

page += Paragraph("October 17, 2020 - October 24, 2020")

page += Heading("Goals For This Week")
page += OrderedList([
    Paragraph("Find out how previous JIT's worked."),
    Paragraph("Create a plan for how my JIT will work based on that."),
])

page += Heading("Journal For This Week")
page += Quote(
    "LuaJIT with the JIT enabled is much faster than all of the other languages benchmarked, including Wren, because Mike Pall is a robot from the future.",
    f"Bob Nystrom, {hyperlink('Wren Benchmarks', 'https://wren.io/performance.html')}"
)

page += Paragraph("Most of my research on JIT's suggests that Bob here has expressed pure truth. LuaJIT is the gold-standard for JIT's.")
page += Paragraph(f"Google has it's own JIT, V8, for Javascript. This is the JIT that runs Javascript in Chrome Browsers (possibly more"
                  f"now that Chromium also runs Edge). It has had millions of dollars invested in it by possibly the techiest tech company there is."
                  f"Nevertheless, it still doesn't even compare to LuaJIT. {hyperlink('Benchmarks', 'http://lua-users.org/lists/lua-l/2010-03/msg00305.html')} "
                  f"indicate that even just the LuaJIT interpreter is faster than the V8 JIT. This suggests that the best model for how a JIT should work is "
                  f"Mike Pall's LuaJIT.")
page += Paragraph(f"""
I should still look at other JIT's though, and how they work. By my research, there are two main methods.
""")
page += Paragraph(f"""
A Tracing JIT is one of them. Essentially, it follows the execution of the program for some amount of time, usually in a 
loop the JIT has noticed is iterated over a lot. After recording one full cycle of that "hot" loop, it compiles what was done
in that loop and replaces the body of that loop with the compiled version. Thus, code that is run a lot is compiled into machine code, 
which makes the code much faster. The targeted aspect of this makes it much more efficient in work down vs speed compared to the other
method of JIT'ing, a method JIT.
""")

page += Paragraph(f"""
A method JIT is the other way to write a JIT Compiler. Essentially, it just compiles a section of code at a time whenever it wants to and executes that
compiled code. The main difference is that it never actually checks what's executed and what isn't, like a tracing jit.
It just compiles all the code all the time. This makes them much simpler to write, and sometimes faster since they don't over-optimize.
{hyperlink("This", "https://news.ycombinator.com/item?id=16204373")} recent discussion covers other aspects of method-jits that
make them more common nowadays. Nevertheless, LuaJIT, a tracing jit, is still better than nearly all method jits.
""")

page += Paragraph(f"""
In summary, a tracing JIT has better best-case performance but worse worst-case performance. A method JIT has more consistent but
worse performance.
""")

page += Paragraph("""
Looking at how PyPy has designed its tracing JIT, I've decided that such a complex means of writing a JIT is probably not for me.
Additionally, having to track exactly what instructions are run seems like a lot of overhead which could slow down the JIT. 
Therefore, I've decided to pursue a method-jit for now. I have time to review this decision later, since I don't start work on the 
actual JIT part of quite a while. 
""")

page += Paragraph("""
Essentially, my plan for my JIT is that it will run normally with an interpreter, but if it sees a function get called a lot, it'll compile and optimize
that function only. This makes it a method JIT, since it doesn't trace that function.
""")

page += Paragraph("Sources:")
page += OrderedList([
    Paragraph(f"{hyperlink('http://lua-users.org/lists/lua-l/2010-03/msg00305.html')}"),
    Paragraph(f"{hyperlink('https://wren.io/performance.html')}"),
    Paragraph(f"{hyperlink('An overview of PyPy, tracing JITs, and meta-tracing JITs', 'http://antocuni.eu/download/antocuni-phd-thesis.pdf')}"),
    Paragraph(f"{hyperlink('https://news.ycombinator.com/item?id=16204373')}")
])

__pages__ = [page]
