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

    def render(self):
        return "".join(element.render() for element in self.elements)


class Element:
    type: str

    def render(self) -> str:
        raise NotImplementedError()


class Text(Element):
    def __init__(self, text: str):
        self.type = "Text"
        self.text = textwrap.dedent(text)

    def render(self) -> str:
        return f'{self.text}'


class Paragraph(Element):
    def __init__(self, text: str):
        self.type = "Paragraph"
        self.text = textwrap.dedent(text)

    def render(self) -> str:
        return f'<div class="content-paragraph"><p>{self.text}</p></div>'


class Title(Element):
    def __init__(self, title_text: str):
        self.type = "Title"
        self.title_text = title_text

    def render(self) -> str:
        return f'<div class="content-title"><header>{self.title_text}</header></div><hr>'


class Code(Element):
    def __init__(self, code: str):
        self.type = "Code"
        self.code = textwrap.dedent(code)

    def render(self) -> str:
        return f'<div class="content-code"><pre>{self.code}</pre></div>'


class OrderedList(Element):
    def __init__(self, items: List[Element]):
        self.type = "OrderedList"
        self.items = items

    def render(self) -> str:
        items = "".join(f'<li class="content-ordered-list-item">{item.render()}</li>' for item in self.items)
        return f'<ol class="content-ordered-list">{items}</ol>'
