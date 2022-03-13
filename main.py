def fast_sort(lst: list) -> list:
    """
    base quick sort algorithm
    :param lst:
    :return:
    """
    if len(lst) < 2:
        return lst
    else:
        # you can get random index from list
        base = lst[0]
        less = [i for i in lst[1:] if i <= base]

        greater = [i for i in lst[1:] if i > base]

        # use recursion function
        return fast_sort(less) + [base] + fast_sort(greater)


def two_indexes_method(lst: list, sum: int) -> list:
    """
    an algorithm for finding the sum of two elements in a list based on the two-index method
    only for sorted lists, you can use fast_sort for sorting your list, or try next solution
    :param lst: some list
    :param sum: some int
    :return: indexes of elements which get a sum
    """
    i = 0
    j = len(lst) - 1
    while i != j:
        if lst[i] + lst[j] == sum:
            return [i, j]
        elif lst[i] + lst[j] > sum:
            j -= 1
        elif lst[i] + lst[j] < sum:
            i += 1
    return []


def sum_of_elements(lst: list, sum: int) -> list:
    """
    Second solution
    :param lst:
    :param sum:
    :return:
    """
    was = {}
    for i in range(len(lst)):
        needed = sum - lst[i]
        if needed in was:
            return [was[needed], i]
        else:
            was.update({lst[i]: i})
    return []


def checking_brackets(lst: list) -> bool:
    """
    A string of brackets is given, you need to check that they are correctly placed
    Example:
    '[{()}]{}' - correct
    '({[}])' - incorrect
    :param lst:
    :return:
    """

    stack = []
    table = {'(': ')', '{': '}', '[': ']'}
    for bracket in lst:
        if bracket in table.keys():
            stack.append(bracket)
        else:
            last_open_bracket = stack.pop()
            if table[last_open_bracket] != bracket:
                return False

    if stack:
        return False

    return True
