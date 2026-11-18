from src.search import search_in_list


def test_search():
    assert search_in_list(["abc", "xyz"], "a") == ["abc"]
