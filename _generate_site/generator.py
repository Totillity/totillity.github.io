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


class NavNode:
    def __init__(self, is_leaf: bool):
        self.is_leaf = is_leaf


class NavTree(NavNode):
    def __init__(self, dir_name: str, children: List[NavNode]):
        super().__init__(False)
        self.dir_name = dir_name
        self.children = children
        self.reachable: List[Path] = []

    def get_child_dir(self, dir_name: str):
        for child in self.children:
            if isinstance(child, NavTree):
                if child.dir_name == dir_name:
                    return child
        raise KeyError(dir_name)

    def add_reachable_path(self, path: Path):
        self.reachable.append(path)

    def create_child_tree(self, dir_name: str):
        self.children.append(NavTree(dir_name, []))

    def create_child_leaf(self, leaf_name: str, leaf_path: str):
        self.children.append(NavLeaf(leaf_name, leaf_path))

    def has_child_dir(self, dir_name: str):
        for child in self.children:
            if isinstance(child, NavTree):
                if child.dir_name == dir_name:
                    return True
        return False


class NavLeaf(NavNode):
    def __init__(self, leaf_name: str, path: str):
        super().__init__(True)
        self.leaf_name = leaf_name
        self.path = path


def render_page(env: jinja2.Environment, page: Page, tree: NavTree):
    template = env.get_template("page_template.html")

    page.path.parent.mkdir(exist_ok=True, parents=True)

    style_link = Path("").joinpath(*Path(relpath(Path("style.css"), page.path)).parts[1:])
    style_link = str(style_link).replace("\\", "/")

    page.path.write_text(template.render(
        elements=page.elements,
        style_link=f"<link rel='stylesheet' href='{style_link}'>",
        nav_tree=tree,
        page_path=page.path
    ))


def main():
    pages = get_pages(get_files())

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader("_templates"),
    )

    Path("style.css").write_text(env.get_template("style.css").render())

    nav_tree = NavTree("root", [])
    for page in pages:
        # create or navigate to each directory needed to get to the page from root
        sub_tree = nav_tree
        sub_tree.add_reachable_path(page.path)
        for part in page.nav_loc[:-1]:
            if not sub_tree.has_child_dir(part):
                sub_tree.create_child_tree(part)
            sub_tree = sub_tree.get_child_dir(part)
            sub_tree.add_reachable_path(page.path)
        # now sub_tree is the parent directory of the page
        sub_tree.create_child_leaf(page.nav_loc[-1], str(page.path).replace("\\", "/"))

    for page in pages:
        render_page(env, page, nav_tree)


if __name__ == '__main__':
    main()
