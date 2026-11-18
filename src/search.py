def search_in_list(items, query):
    return [x for x in items if query in x]


def search_numbers(numbers, minimum):
    return [n for n in numbers if n >= minimum]
