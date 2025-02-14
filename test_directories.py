import pytest

from directories import Directory

def test_add():
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

def test_delete():
    root = Directory("")
    root.add("fruits/apples/fuji")
    root.delete("fruits/apples/fuji")
    assert "fuji" not in root.child["fruits"].child["apples"].child
    assert "apples" in root.child["fruits"].child # should only delete specified

    root.delete("fruits/apples")
    assert "apples" not in root.child["fruits"].child # now it should be deleted

def test_delete_non_existent(capsys):
    root = Directory("")
    root.add("fruits/apples")

    root.delete("fruits/oranges") # should not raise an error
    captured = capsys.readouterr().out.strip()
    expected = "Cannot delete fruits/oranges - oranges does not exist"
    assert captured == expected

    root.delete("vegetables/carrots") # should not raise an error
    next_captured = capsys.readouterr().out.strip()
    next_expected = "Cannot delete vegetables/carrots - vegetables does not exist"
    assert next_captured == next_expected

def test_move():
    root = Directory("")
    root.add("fruits/apples")
    root.add("vegetables")
    root.move("fruits/apples", "vegetables")
    assert "apples" in root.child["vegetables"].child
    assert "fruits" in root.child and "apples" not in root.child["fruits"].child


