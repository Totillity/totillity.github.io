from _generate_site.elements import *

page = Page("index.html", nav_loc=["Contents"])

page += Title("Introduction")

page += Paragraph(f"""
Before you read this, you should know what I mean for this book to be. It is intended as a repository of the information
I have gathered on making programming languages. While that is much more than I started with, it's not even close to everything.
There's a {italics("lot")} more out there. Like a {italics("lot")}. For example, I don't cover what Rust and related languages do
to ensure that all memory is accounted for before you even run your program, because I've never implemented such a system.
I don't cover
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


__pages__ = [page]
