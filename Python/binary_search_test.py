"""Main tests module."""

from binary_search import binary_search


def test_binary_search():
    """Test binary_search."""
    item_list = [1, 2, 3, 5, 8]

    item = 6
    exists = binary_search(item, item_list)
    assert exists is False

    item = 5
    exists = binary_search(item, item_list)
    assert exists is True
