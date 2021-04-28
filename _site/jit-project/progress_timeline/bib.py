from _generate_site.elements import *

page = Page("jit-project/progress-timeline/bibliography.html",
            nav_loc=["JIT Project", "Progress Timeline", "[11] Bibliography"])

page += Title("Bibliography")

page += Paragraphs("""
Nystrom, Bob. “Performance.” Wren, wren.io/performance.html. Accessed 17 Aug. 2020.

Intel. Intel® 64 and IA-32 Architectures Software Developer’s Manual. Vol. 2, Intel, 2016, www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-instruction-set-reference-manual-325383.pdf.

Tan, Paul. “Encoding X86-64 Instructions: Some Worked Examples.” Pyokagan’s Devlog, 20 Sept. 2016, pyokagan.name/blog/2019-09-20-x86encoding.

Bendersky, Eli. “How to JIT - an Introduction.” Eli Bendersky’s Website, 5 Nov. 2013, eli.thegreenplace.net/2013/11/05/how-to-jit-an-introduction.

“Coder64-Abc.” X86 Opcode and Instruction Reference, 18 Feb. 2017, ref.x86asm.net/coder64-abc.html.

“X86-64 Instruction Encoding.” OSDev Wiki, 2014, wiki.osdev.org/X86-64_Instruction_Encoding.

“What Is between ESP and EBP?” Stack Overflow, 22 Feb. 2013, stackoverflow.com/questions/15020621/what-is-between-esp-and-ebp.

Wikipedia contributors. “Function Prologue.” Wikipedia, 21 Jan. 2021, en.wikipedia.org/wiki/Function_prologue.

“Ask HN: Have Tracing JIT Compilers Lost?” Hacker News, 22 Jan. 2018, news.ycombinator.com/item?id=16204373.

Pall, Mike. “Re: New LuaJIT Benchmark Results (Was Re: [ANN] LuaJIT-2.0.0-Beta3).” Lua Users Archive, 10 Mar. 2010, lua-users.org/lists/lua-l/2010-03/msg00305.html.

Llvmlite Documentaion. llvmlite, llvmlite.readthedocs.io/en/latest. Accessed 17 Aug. 2020.

Python. “Dis — Disassembler for Python Bytecode.” Python 3.9.4 Documentation, docs.python.org/3/library/dis.html. Accessed 21 Aug. 2020.

Wikipedia contributors. “Category:Parsing Algorithms.” Wikipedia, en.wikipedia.org/wiki/Category:Parsing_algorithms. Accessed 15 Jan. 2021.

Nystrom, Bob. “Parsing Expressions.” Crafting Interpreters, www.craftinginterpreters.com/parsing-expressions.html. Accessed 17 Nov. 2020.

---. “Constant Folding.” Wikipedia, 8 Apr. 2021, en.wikipedia.org/wiki/Constant_folding.

---. “Dead Code Elimination.” Wikipedia, 20 Apr. 2021, en.wikipedia.org/wiki/Dead_code_elimination.

---. “Instruction Selection.” Wikipedia, 10 Dec. 2020, en.wikipedia.org/wiki/Instruction_selection.

“Conditional (Ternary) Operator.” JavaScript | MDN, 14 Apr. 2021, developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator.

“6. Expressions.” Python 3.9.4 Documentation, docs.python.org/3/reference/expressions.html?highlight=ternary#conditional-expressions. Accessed 17 Nov. 2020.

---. “Static Single Assignment Form.” Wikipedia, 20 Apr. 2021, en.wikipedia.org/wiki/Static_single_assignment_form#Computing_minimal_SSA_using_dominance_frontiers.

Allen, Ian D. “The CARRY Flag and OVERFLOW Flag in Binary Arithmetic.” Teaching.Idallen, teaching.idallen.com/dat2343/10f/notes/040_overflow.txt. Accessed 17 Nov. 2020.

---. “Smalltalk.” Wikipedia, 8 Apr. 2021, en.wikipedia.org/wiki/Smalltalk.

---. “JavaScript.” Wikipedia, 19 Nov. 2001, en.wikipedia.org/wiki/JavaScript.

Nystrom, Bob. “Optimization.” Crafting Interpreters, www.craftinginterpreters.com/optimization.html#nan-boxing. Accessed 21 Mar. 2021.

Zuiderkwast. “Zuiderkwast/Nanbox.” GitHub, 11 Sept. 2013, github.com/zuiderkwast/nanbox.

“Programming Languages Benchmarks.” Attractivechaos, June 2011, attractivechaos.github.io/plb.
""")


__pages__ = [page]
