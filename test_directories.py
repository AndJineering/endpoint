import pytest

from directories import Directory

def test_create():
    root = Directory("")
    root.add("fruits/apples/fuji")
    assert "fruits" in root.child
    assert "apples" in root.child["fruits"].child
    assert "fuji" in root.child["fruits"].child["apples"].child

def test_list_sorted(capsys):
    # Each level of a directory should be sorted
    root = Directory("")
    root.add("vegetables")
    root.add("fruits")
    root.add("fruits/bananas")
    root.add("fruits/apples")
    
    root.list()
    captured = capsys.readouterr().out.strip()

    expected = """\
fruits
  apples
  bananas
vegetables"""

    assert captured == expected





