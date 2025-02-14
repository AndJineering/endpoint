import pytest

from directories import Directory

def test_create():
    root = Directory("")
    root.add("fruits/apples/fuji")
    assert "fruits" in root.child
    assert "apples" in root.child["fruits"].child
    assert "fuji" in root.child["fruits"].child["apples"].child
