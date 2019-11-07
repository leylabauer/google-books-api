from main import *

booksearch = bookSearching()
userinput = userInput()
printtocl = printToCL()
userinputrules = userInputRules()
bookinfo = booksearch.bookinfo

# To run the tests, the objects in main.py cannot be instantiated.
# Comment them out to properly run the tests.


def test_if_selected_book_is_int_is_true():
    assert userinputrules.check_if_selected_book_is_int(2) is True

def test_if_selected_book_is_int_is_true():
    assert userinputrules.check_if_selected_book_is_int("text") is False

def test_if_search_is_empty():
    bookinfo.update({1: ["No title listed", "No authors listed", "No publisher listed"]})
    assert userinputrules.check_if_search_is_empty(bookinfo) is True

def test_if_search_is_empty():
    bookinfo.update({1: ["Cats", "Desmond Bauer", "Meowing House Rules"]})
    assert userinputrules.check_if_search_is_empty(bookinfo) is False