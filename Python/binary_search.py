"""
Binary search module
"""


def binary_search(item, item_list):
    """Binary search implementation

    Parameters:
    item_list (list): an array of integers
    item (integer): the value we are looking for in the item_list

    Returns:
    bool: the index of the given item

   """
    first = 0
    last = len(item_list) - 1
    found = False
    while first <= last and found is False:
        mid = (first + last) // 2
        if item_list[mid] == item:
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found
