from _generate_site.elements import *

page = Page("index.html", nav_loc=["Contents"])

page += Title("Introduction")

page += Paragraph(f"""
This is a site I made in about three days, so it's not perfect, although I am constantly improving it. 
If you think anything could be improved, please tell me so I can do so.
""")

page += Paragraph(f"""
You can examine my horrible code for this site on {hyperlink("Github", "https://github.com/Totillity/totillity.github.io")}. 
It is auto-generated by {inline_code("/_generate_site/generator.py")} called with the command-line argument 
{inline_code("dir=_site")}.  The site template files used to generate it can be found in {inline_code("/_site")}.
""")

page += Paragraph(f"""
You can navigate using the dropdown menus on the side. To not get lost, try dropping bread crumbs whenever you
click a link, so you can always follow those back to here.
""")


__pages__ = [page]
