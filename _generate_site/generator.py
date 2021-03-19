from __future__ import annotations

import argparse
from typing import List, IO, Tuple
from pathlib import Path
from os.path import relpath
import re

import jinja2

from _generate_site.elements import Page


def get_pages(files: List[IO]) -> List[Page]:
    to_render = []
    for file in files:
        text = file.read()
        mod_globals = {}
        exec(text, mod_globals)
        to_render.extend(mod_globals.get('__pages__', []))
    return to_render


class NavNode:
    order_regex = re.compile(r"\[[0-9]+]")

    def __init__(self, nav_name: str, nav_order: int, is_leaf: bool):
        self.nav_name = nav_name
        self.nav_order = nav_order
        self.is_leaf = is_leaf

    @classmethod
    def get_parts(cls, nav_pos: str) -> Tuple[str, int]:
        if match := cls.order_regex.match(nav_pos):
            return match.string[match.end():].strip(), int(match.group()[1:-1])
        else:
            return nav_pos, -1


class NavTree(NavNode):
    def __init__(self, nav_pos: str, children: List[NavNode]):
        name, order = self.get_parts(nav_pos)
        super().__init__(name, order, False)
        self.children = children
        self.reachable: List[Path] = []

    def get_child_dir(self, nav_pos: str):
        dir_name, _ = self.get_parts(nav_pos)
        for child in self.children:
            if isinstance(child, NavTree):
                if child.nav_name == dir_name:
                    return child
        raise KeyError(dir_name)

    def add_reachable_path(self, path: Path):
        self.reachable.append(path)

    def create_child_tree(self, nav_pos: str):
        dir_name, order = self.get_parts(nav_pos)

        insert_loc = 0
        for n, item in enumerate(self.children):
            if item.nav_order >= order:
                insert_loc = n
        else:
            insert_loc = len(self.children)

        self.children.insert(insert_loc, NavTree(nav_pos, []))

    def create_child_leaf(self, nav_pos: str, leaf_path: str):
        dir_name, order = self.get_parts(nav_pos)

        insert_loc = 0
        for n, item in enumerate(self.children):
            if item.nav_order >= order:
                insert_loc = n
                break
        else:
            insert_loc = len(self.children)

        self.children.insert(insert_loc, NavLeaf(nav_pos, leaf_path))

    def has_child_dir(self, nav_pos: str):
        dir_name, _ = self.get_parts(nav_pos)
        for child in self.children:
            if isinstance(child, NavTree):
                if child.nav_name == dir_name:
                    return True
        return False


class NavLeaf(NavNode):
    def __init__(self, nav_pos: str, path: str):
        name, order = self.get_parts(nav_pos)
        super().__init__(name, order, True)
        self.path = path


def render_page(env: jinja2.Environment, page: Page, tree: NavTree):
    template = env.get_template("page_template.html")

    page.path.parent.mkdir(exist_ok=True, parents=True)

    style_link = Path("").joinpath(*Path(relpath(Path("style.css"), page.path)).parts[1:])
    style_link = str(style_link).replace("\\", "/")

    page.path.write_text(template.render(
        page=page,
        style_link=f"<link rel='stylesheet' href='{style_link}'>",
        nav_tree=tree,
        page_path=page.path
    ))


def main():
    argparser = argparse.ArgumentParser("site renderer")
    argparser.add_argument("files", nargs="*", type=argparse.FileType("r"))
    argparser.add_argument("-I", "--include-dir", type=Path, action="append")
    argparser.add_argument("-D", "--dest-dir", type=Path)

    parsed = argparser.parse_args()
    files = []
    files.extend(parsed.files)
    for dir in parsed.include_dir:
        files.extend(path.open("r") for path in dir.glob("**/*.py"))
    pages = get_pages(files)

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
