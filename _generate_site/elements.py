from __future__ import annotations

import textwrap
from pathlib import Path
from typing import List


def italics(s: str) -> str:
    return f"<i>{s}</i>"


def hyperlink(s: str, link_to: str = None) -> str:
    if link_to is None:
        link_to = s
    return f'<a href="{link_to}">{s}</a>'


def inline_code(s: str) -> str:
    return f"<code>{s}</code>"


class Page:
    def __init__(self, path: str, nav_loc: List[str]):
        self.path = Path(path)
        self.nav_loc = nav_loc

        self.elements: List[Element] = []

    def __iadd__(self, other: Element):
        self.elements.append(other)
        return self


class Element:
    type: str


class Paragraph(Element):
    def __init__(self, text: str):
        self.type = "Paragraph"
        self.text = textwrap.dedent(text)


class Title(Element):
    def __init__(self, title_text: str):
        self.type = "Title"
        self.title_text = title_text


class Code(Element):
    def __init__(self, code: str):
        self.type = "Code"
        self.code = textwrap.dedent(code)