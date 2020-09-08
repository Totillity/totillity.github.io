from __future__ import annotations

import argparse
from typing import List, IO, Dict, Any
from pathlib import Path, PosixPath
from os.path import relpath

import jinja2

from _generate_site.elements import Page


def get_files() -> List[IO]:
    argparser = argparse.ArgumentParser("site renderer")
    argparser.add_argument("file", nargs="*", type=argparse.FileType("r"))
    argparser.add_argument("--dir", nargs="*", type=str)

    parsed = argparser.parse_args()
    files = []
    files.extend(parsed.file)
    for dir in parsed.dir:
        files.extend(path.open("r") for path in Path(dir).glob("**/*.py"))
    return files


def get_pages(files: List[IO]) -> List[Page]:
    to_render = []
    for file in files:
        text = file.read()
        mod_globals = {}
        exec(text, mod_globals)
        to_render.extend(mod_globals['__pages__'])
    return to_render


def render_page(env: jinja2.Environment, page: Page, tree: Dict[str, Any]):
    template = env.get_template("page_template.html")

    page.path.parent.mkdir(exist_ok=True, parents=True)

    style_link = Path("").joinpath(*Path(relpath(Path("style.css"), page.path)).parts[1:])
    style_link = str(style_link).replace("\\", "/")

    page.path.write_text(template.render(
        elements=page.elements,
        style_link=f"<link rel='stylesheet' href='{style_link}'>",
        nav_tree=tree.items(),
    ))


def main():
    pages = get_pages(get_files())

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader("_templates"),
    )

    Path("style.css").write_text(env.get_template("style.css").render())
    nav_tree = {}
    for page in pages:
        sub_tree = nav_tree
        for item in page.nav_loc[:-1]:
            if item not in sub_tree:
                sub_tree[item] = {}
            sub_tree = sub_tree[item]

        sub_tree[page.nav_loc[-1]] = str(page.path).replace("\\", "/")

    for page in pages:
        render_page(env, page, nav_tree)


if __name__ == '__main__':
    main()
