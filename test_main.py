from main import *

booksearching = BookSearching()
readingList = ReadingList()
userinput = UserInput()
print_ = Print()
rules = Rules()
runningprogram = RunProgram(booksearching, readingList, userinput, print_, rules)
book_info = booksearching.book_info
reading_list = readingList.reading_list

def test_is_selected_book_integer_is_true():
    assert rules.is_selected_book_integer(2) is True

def test_is_selected_book_integer_is_false():
    assert rules.is_selected_book_integer("text") is False

def test_is_selected_book_in_book_info_is_true():
    assert rules.is_selected_book_in_book_info(3) is True

def test_is_selected_book_in_book_info_is_false():
    assert rules.is_selected_book_in_book_info(6) is False

def test_is_search_empty_is_false():
    book_info.update({1: ["Cats", "Desmond Bauer", "Meowing House Publishing"]})
    assert rules.is_search_empty(book_info) is False

def test_is_search_empty_is_true():
    book_info.update({1: ["No title listed", "No authors listed", "No publisher listed"]})
    assert rules.is_search_empty(book_info) is True

def test_is_searchtype_valid_is_true():
    assert rules.is_searchtype_valid("intitle") is True

def test_is_searchtype_valid_is_false():
    assert rules.is_searchtype_valid("text") is False

def test_is_reading_list_empty_is_true():
    assert rules.is_reading_list_empty(reading_list) is True

def test_add_to_reading_list_works():
    book_info.update({1: ["Cats", "Desmond Bauer", "Meowing House Publishing"]})
    readingList.add_to_reading_list(1, book_info)
    assert len(reading_list) is 1

def test_is_reading_list_empty_is_false():
    assert rules.is_reading_list_empty(reading_list) is False