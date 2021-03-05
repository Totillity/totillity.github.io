from _generate_site.elements import *

page = Page("jit-project/progress-timeline/journal-2.html", nav_loc=["JIT Project", "Progress Timeline", "[4] Journal 2"])

page += Title("Journal 2: Weeks 4-7")

page += Paragraph("November 7, 2020 - January 15, 2021")

page += Heading('Goals for this Journal:')
page += OrderedList([
    Paragraph('Implement the previous IR into my assembler'),
    Paragraph('Test that IR'),
    Paragraph('Ensure I fully implement the IR'),
    Paragraph('Look through current languages and see what I want mine to look like'),
    Paragraph('Based on my previous work, I can see what language design would lend itself best to JITing'),
    Paragraph('Design such a language'),
    Paragraph('Implement Parsing for the language'),
    Paragraph('Research better error handling and ast representation. Advisor could help a lot here.'),
    Paragraph('Learn how to do the above in C'),
    Paragraph('Implement a way to generate the IR from the frontend'),
    Paragraph('Out of all the steps so far, this is the most likely to either fail or work poorly.'),
    Paragraph('Therefore, also use this week to implement all the improvements and fixes I’ve thought of over the past 7 weeks'),
])

page += Heading("Research")

page += Paragraphs(f"""
{bold("Note: all references labelled at the bottom.")}
{bold("Note: I used code snippets instead of screenshots because this is a programming project.")}
{bold("Note: I used pseudocode instead of actual C for the sake of clarity.")}

Over these past four weeks of goals, my primary object was to get some sort of front-end for my assembly compiler working.
I am proud to say that I have achieved that overarching goal.

First, let me define what I mean by "front-end". Know that this isn't an exactly defined term. Everyone will have their own. 
In my mind, I define a front-end as the code which transform text like "print(10)" into an IR, which I've defined in the previous journal.
Parsing is the name of this task of converting raw text to a structure which represents a program (an IR).

There are many different parsing techniques. LR Parser, Packrat parsing, Earley parser, the list is nearly endless (and linked to in the description).
I've tried many of them, but I always return to Recursive descent parsers, because it is very simple and easy to extend,
although also very limited. 

The concept of Recursive descent is simple. You take the file and split it into "tokens". A token is the smallest unit of text which
logically fits together. I assign a type to each token, too. So, for example, "print 1 + foo.bar()" becomes:
""")

page += Code("""
TOKEN(type="identifier", text="print")
TOKEN(type="number", text="1")
TOKEN(type="plus", text="+")
TOKEN(type="identifier", text="foo")
TOKEN(type="dot", text=".")
TOKEN(type="identifier", text="bar")
TOKEN(type="left parenthesis", text="(")
TOKEN(type="right parenthesis", text=")")
""")

page += Paragraphs(f"""
The algorithm needed to do this tokenization step is not complex. Just look at the current character, decide what type of 
token it must belong to, and eat a character until that token type must be done. For example, to tokenize an identifier:
""")

page += Code("""
if (current_character is in "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
    // then we are looking at an identifier
    identifier_text = "";
    while (current_character is in "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        add current_character to the end of identifier_text; 
        current_character = next_character();
    }
    create_token(type="identifier", text=identifier_text);
}
""")

page += Paragraphs(f"""
It is even simpler to tokenize anything else.

We now have a list of tokens after apply this process to the whole file. The next step is, as I mentioned before,
converting that list of tokens into an IR. Once again, this process is simple enough, though it might take a few tries
to really wrap your head around. 

The best was to understand what a recursive descent parser does is to follow it as it works its magic. We start off at 
'parse_file': 
""")

page += Code("""
def parse_file() {
    current_token = get_current_token();
    while (current_token.type is not END_OF_FILE) {
        // when we reach the end of the file (which is when we know to stop), the tokenizer will emit an END_OF_FILE token
        // therefore, when we reach that token in the parser, we know to stop parsing
        
        if (current_token.type == "def") {
            // if we see a "def" token, which always means a function definition always follows
            // therefore, goto a function which can parse that function
            parse_function();
        } else (current_token.type == "class") {
            // if we see a "class" token, which always means a class definition always follows
            // therefore, goto a function which can parse that class
            parse_class();
        } else {
            // we see something weird, so yell about it
            show_error_and_quit("Expected a def or class");
        }
    }
}
""")

page += Paragraphs(f"""
The key insight (or trick, depending on your perspective) of Recursive descent parsers is that you can always know what
to do given just one token. If you take Python, for example, when you see "def", you always know that a function is going to follow that "def".
This means a Recursive descent parser doesn't have to do anything weird like going backwards when its made a mistake or
maintaining a stack to account for all possibilities. In a Recursive descent parser, it {italics("cannot make a mistake")}.
Of course, this comes at the cost of designing a language such that you can always know what follows from just one token.
This influenced a lot of Python and related language's designs. If you take Haskell, which uses a much more advanced parser,
you can see how the flexibility offered by that parser afforded much more flexibility and complexity in the language design.  

Anyways, onto the code for parse_function():
""")

page += Code("""
def parse_function() {
    expect_token("def");
    // What does "expect_token()" do, you might ask?      
    // if the current token is a "def" token, move the token list forwards by one, 
    //   so the next current_token is the token after the def token, then return the "def" token
    // if the current token is not a "def" token, show an error and quit
    
    function_name = expect_token("identifier");
    
    expect_token("left parenthesis");
    // parse the arguments ...
    // boring and confusing code, honestly
    expect_token("right parenthesis");
    
    expect_token("left brace");
    while (next_token() is not "right_brace") {
        parse_statement();
    }
    expect_token("right brace");
}
""")

page += Paragraphs("""
Most pretty standard code. Once again, we go into an inner function. See where the "recursive" part of recursive descent comes from?
""")

page += Code("""
def parse_statement() {
    current_token = current_token();
    if (current_token.type == "return") {
        parse_return();
    } else if (current_token.type == "let") {
        parse_let();
    } else if (current_token.type == "if") {
        parse_if();
    } 
    // ... snip ...
    } else {
        // we see something weird, so yell about it
        show_error_and_quit("Expected a statement");
    }
}
""")

page += Paragraphs(f"""
Looks a bit like the inside of the loop of from parse_file, expect with different expected tokens and functions. Once again,
we use the insight that if we see a "return", then the next few tokens {italics("must")} be part of a return statement. Let's
examine the code that parses the return statement. Trust me, we're almost at the most interesting part.
""")

page += Code("""
def parse_return() {
    expect_token("return");
    expr = parse_expression();
}
""")

page += Paragraphs("""
The most complicated part of a Recursive descent parser lies in that unassuming function call: "parse_expression".

What's an expressions? Stuff like "a+b" or "foo.bar()". The weirdest part of expressions is how nested they can become.
"1" is technically a complete expression. However, "1 * 3" is also an expression, which is made up of two smaller expressions,
"1" and "2", and a relation between them, "*". 

The real difficulty here is seen in the expression "1 + 3 * 2". If you strictly parsed them in order as we have done is all the
above code snippets, you'd get a IR which said to first add 1 and 3, then multiply 2 to the result of that, to get 8.
This is clearly wrong to anyone who's done any math. We really should multiply 3 and 2 first, then add 1 to the result, to get 7.
However, to do so, we would need to parse in an order different from first to last. 

Recursive descent parsers have a method of dealing with this. We create a different function for each level of precedence (so,
a function for all addition and subtraction, a function for all multiplication, and so on for all other expressions in you language).
Each level first immediately delegates to the level below, then tries it's level. As an example: 
""")

page += Code("""
def parse_expression() {
    // in this example, expressions aren't very complicated, so immediately delegate to addition
    return parse_addition();
}

def parse_addition() {
    expr = parse_multiplication()
    
    while (next_token is "+" or "-") {
        if (next_token is "+") {
            expect("+");
            right = parse_multiplication();
            expr = add(expr, right);
        } else if (next_token is "-") {
            expect("-");
            right = parse_multiplication();
            expr = sub(expr, right);
        }
    }
    return expr;
}

def parse_multiplication() {
    expr = parse_terminal();
    // parse_terminal just returns a identifier or number if it exists
    
    while (next_token is "*" or "/") {
        if (next_token is "*") {
            expect("*");
            right = parse_terminal();
            expr = mul(expr, right);
        } else if (next_token is "/") {
            expect("/");
            right = parse_terminal();
            expr = div(expr, right);
        }
    }
    return expr;
}
""")

page += Paragraphs("""
Let's try following what this code will do given "1 + 2 * 3".
""")

page += OrderedList([
    Paragraph("""parse_expression goes to parse_addition"""),
    Paragraph("""parse_addition goes to parse_multiplication"""),
    Paragraph("""parse_multiplication goes to parse_terminal"""),
    Paragraph("""parse_terminal return 1"""),
    Paragraph("""parse_multiplication doesn't see a * or /, so it returns just the 1"""),
    Paragraph("""parse_multiplication does see a +, so it takes the + and goes back into parse_multiplication"""),
    Paragraph("""parse_multiplication goes to parse_terminal"""),
    Paragraph("""parse_terminal return 2"""),
    Paragraph("""parse_multiplication does see a *, so it takes the * and goes back into parse_terminal"""),
    Paragraph("""parse_terminal return 3"""),
    Paragraph("""parse_multiplication combines the 2 and 3 into (2 * 3)"""),
    Paragraph("""parse_multiplication doesn't see a * or /, so it returns the (2 * 3)"""),
    Paragraph("""parse_addition combines the 1 and (2 * 3) into (1 + (2 * 3))"""),
    Paragraph("""parse_addition doesn't see a + or -, so it returns the (1 + (2 * 3))"""),
])

page += Paragraphs("""
As you can see, we've got the expression with the right precedence. You can give it any expression and see that it comes to the correct result.
It handles everything right, even case of repeated addition like "1 + 2 + 3", where the correct order is "(1 + 2) + 3".

This is the basics of a Recursive descent parser. With this basis, we can parse nearly anything. This is also how my front-end works.
In each of the above functions, it also includes the code to emit the right IR as it goes, so I can generate IR from text now.
That IR can be pumped directly into the compiler my last Journal was about, so the first half of my project is now done. 
""")

page += Heading("Reflection")
page += Paragraphs(f"""
I didn't do nearly as much as I wanted to over break. I also couldn't make this journal nearly as nice as I wanted. This 
one uses way more specific terminology than I wanted, and assumes a greater understanding of coding with the pseudo-code.
I hope it's still accessible. I also spent way too much trying to figure out how to include a screenshot or something like it,
which is part of the reason my journal is so late.

Going forward, things are looking much brighter. All my previous work is on ground I've tread many times before. Everything
that I've yet to work on is new, so you can look forward to actual research sections and much more lively prose.
""")

page += Heading("Main Accomplishments")
page += OrderedList([
    Paragraphs("Created lexer (tokenizer)"),
    Paragraphs("Created parser"),
    Paragraphs("Solved assign problem which bugged me for a while (solution: pass an lvalue flag)"),
    Paragraphs("Hooked parser and compiler together, they work mostly fine"),
    Paragraphs("Improved the structure of the compiler code"),
])

page += Heading("Sources:")
page += OrderedList([
    Paragraph(hyperlink("Wikipedia's list of parsing algorithms", "https://en.wikipedia.org/wiki/Category:Parsing_algorithms")),
    Paragraph(hyperlink("Another method of parsing I experimented with back in the day", "https://lark-parser.readthedocs.io/en/latest/")),
    Paragraph(hyperlink("My primary resource on Recursive descent", "http://www.craftinginterpreters.com/parsing-expressions.html")),
    Paragraph(hyperlink("Haskell homepage, where you can see the differences in language", "https://www.haskell.org/")),
])

__pages__ = [page]
