from main import *

booksearch = bookSearching()
userinput = userInput()
printtocl = printToCL()
userinputrules = userInputRules()
bookinfo = booksearch.bookinfo
reading_list = booksearch.reading_list

# To run the tests, the objects in main.py cannot be instantiated.
# Comment them out to properly run the tests.

def test_if_selected_book_is_int_is_true():
    assert userinputrules.check_if_selected_book_is_int(2) is True

def test_if_selected_book_is_int_is_false():
    assert userinputrules.check_if_selected_book_is_int("text") is False

def test_if_selected_book_is_in_list_is_true():
    assert userinputrules.check_if_selected_book_int_is_in_list(3) is True

def test_if_selected_book_is_in_list_is_false():
    assert userinputrules.check_if_selected_book_int_is_in_list(6) is False

def test_if_search_is_empty():
    bookinfo.update({1: ["Cats", "Desmond Bauer", "Meowing House Publishing"]})
    assert userinputrules.check_if_search_is_empty(bookinfo) is False

def test_if_search_is_empty():
    bookinfo.update({1: ["No title listed", "No authors listed", "No publisher listed"]})
    assert userinputrules.check_if_search_is_empty(bookinfo) is True

def test_if_searchtype_input_is_accurate_returns_true():
    assert userinputrules.check_if_searchtype_input_is_accurate('intitle') is True

def test_if_searchtype_input_is_accurate_returns_false():
    assert userinputrules.check_if_searchtype_input_is_accurate('text') is False

def test_add_selected_book_to_reading_list_works():
    bookinfo.update({1: ["Cats", "Desmond Bauer", "Meowing House Publishing"]})
    booksearch.add_selected_book_to_reading_list(1, bookinfo)
    assert len(reading_list) is 1
