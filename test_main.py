from main import *

booksearching = BookSearching()
readingList = ReadingList()
userinput = UserInput()
print_ = Print()
rules = Rules()
bookinfo = booksearching.bookinfo
reading_list = booksearching.reading_list

# To run the tests, the objects in main.py cannot be instantiated.
# Comment them out to properly run the tests.

def test_is_selected_book_integer_is_true():
    assert Rules.is_selected_book_integer(2) is True

def test_if_selected_book_is_int_is_false():
    assert Rules.check_if_selected_book_is_int("text") is False

def test_if_selected_book_is_in_list_is_true():
    assert Rules.check_if_selected_book_int_is_in_list(3) is True

def test_if_selected_book_is_in_list_is_false():
    assert Rules.check_if_selected_book_int_is_in_list(6) is False

def test_if_search_is_empty():
    bookinfo.update({1: ["Cats", "Desmond Bauer", "Meowing House Publishing"]})
    assert Rules.check_if_search_is_empty(bookinfo) is False

def test_if_search_is_empty():
    bookinfo.update({1: ["No title listed", "No authors listed", "No publisher listed"]})
    assert Rules.check_if_search_is_empty(bookinfo) is True

def test_if_searchtype_input_is_accurate_returns_true():
    assert Rules.check_if_searchtype_input_is_accurate('intitle') is True

def test_if_searchtype_input_is_accurate_returns_false():
    assert Rules.check_if_searchtype_input_is_accurate('text') is False

def test_if_reading_list_is_empty_returns_true():
    assert Rules.check_if_reading_list_is_empty(reading_list) is True

def test_add_selected_book_to_reading_list_works():
    bookinfo.update({1: ["Cats", "Desmond Bauer", "Meowing House Publishing"]})
    booksearching.add_selected_book_to_reading_list(1, bookinfo)
    assert len(reading_list) is 1

def test_if_reading_list_is_empty_returns_false():
    assert Rules.check_if_reading_list_is_empty(reading_list) is False