import json
import requests
import sys

class BookSearching:

    def __init__(self, book_info = {}, data = {}):
        self.book_info = book_info
        self.data = data

    def search_for_books(self, text, searchtype, keyword):
        if searchtype == "no":
            response = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + keyword + '&key=AIzaSyCU2dyXMyOEp9rhcYonOmrhQ_ugikWyi9s')
            self.data = json.loads(response.text)
        elif text == "no":
            response = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + searchtype + ':' + keyword + '&key=AIzaSyCU2dyXMyOEp9rhcYonOmrhQ_ugikWyi9s')
            self.data = json.loads(response.text)
        else: 
            response = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + text + '+' + searchtype + ':' + keyword + '&key=AIzaSyCU2dyXMyOEp9rhcYonOmrhQ_ugikWyi9s')
            self.data = json.loads(response.text)
        return self.data

    def select_five_books(self, data):
        j = 1
        for i in range(5):
            try: 
                title = data["items"][i]["volumeInfo"]["title"]
            except:
                title = "No title listed"
            try:
                author = data["items"][i]["volumeInfo"]["authors"]
            except:
                author = "No authors listed"
            try: 
                publisher = data["items"][i]["volumeInfo"]["publisher"]
            except:
                publisher = "No publisher listed"
            self.book_info.update({j: [title, author, publisher]})
            j += 1
        return self.book_info


class ReadingList:

    def __init__(self, reading_list = {}):
        self.reading_list = reading_list

    def add_to_reading_list(self, selected_book, book_info):
        book_to_add = book_info[int(selected_book)]
        book_number = len(self.reading_list) + 1
        self.reading_list.update({book_number: book_to_add})


class UserInput:

    def __init__(self, text="", searchtype="", keyword=""):
        self.text = text
        self.searchtype = searchtype
        self.keyword = keyword

    def get_search_text(self):
        text = input("Is there an additional keyword to help with your search? If not, enter 'no'. ")
        return text.lower()
        
    def get_search_type(self):
        searchtype = input("Is this keyword related to the author, the subject, the title, or the publisher? Enter 'inauthor', 'insubject', 'intitle', 'inpublisher', or 'no'. ")
        return searchtype.lower()

    def get_search_keyword(self):
        keyword = input("What keyword do you want to look up? ")
        return keyword.lower()

    def get_user_command(self):
        answer = input("Do you want to search for a book, select a book from a search to add to your reading list, view your reading list, or exit? Enter 'search', 'select', 'view', or 'exit'. ")
        return answer.lower()

    def select_a_book(self):
        selected_book = input("What book number do you want to select? ")
        return selected_book


class Rules:

    def __init__(self):
        pass

    def is_selected_book_integer(self, selected_book):
        try:
            if type(int(selected_book)) is int:
             return True
        except ValueError:
            return False

    def is_selected_book_in_book_info(self, selected_book):
        if int(selected_book) in [1,2,3,4,5]:
            return True
        else:
            return False

    def is_search_empty(self, book_info):
        if len(book_info) == 0:
            return True
        elif book_info[1] == ["No title listed", "No authors listed", "No publisher listed"]:
            return True
        else:
            return False

    def is_searchtype_valid(self, searchtype):
        if searchtype in ['inauthor', 'insubject', 'intitle', 'inpublisher']:
            return True
        else:
            return False

    def is_reading_list_empty(self, reading_list):
        if len(reading_list) == 0:
            return True
        else:
            return False


class Print:

    def __init__(self):
        pass

    def print_book_info(self, book_info):
        j = 1
        for item in book_info:
            print('Book #' + str(j) + ':')
            print('Title: ' + book_info[j][0])
            print('Author(s): ')
            if type(book_info[j][1]) == list:
                for auth in book_info[j][1]:
                    print(auth)
            else:
                print(book_info[j][1])
            print('Publisher: ' + book_info[j][2])
            print("***")
            j += 1

    def print_reading_list(self, reading_list):
        j = 1
        for item in reading_list:
            print('Book #' + str(j) + ':')
            print('Title: ' + reading_list[j][0])
            print('Author(s): ')
            if type(reading_list[j][1]) == list:
                for auth in reading_list[j][1]:
                    print(auth)
            else:
                print(reading_list[j][1])
            print('Publisher: ' + reading_list[j][2])
            print("***")
            j += 1

    def print_statement(self, statement):
        print('*' * 6)
        print(statement)
        print('*' * 6)


class RunProgram:

    def __init__(self, book_searching, readingList, user_input, print_, rules):
        self.book_searching = book_searching
        self.readingList = readingList
        self.user_input = user_input
        self.print_ = print_
        self.rules = rules

    def start_program(self):
        self.print_.print_statement("Welcome to the Google Books Command Line Search! To exit the program, type 'exit'. ")
        self.ask_user()

    def ask_user(self):
        user_command = self.user_input.get_user_command()
        if user_command == 'search':
            self.search_for_books()
        elif user_command == 'exit':
            self.exit_program()
        elif user_command == 'select':
            self.select_book()
        elif user_command == 'view':
            self.view_reading_list()
        else:
            self.print_.print_statement("Hmm, I don't have that option. Please enter 'search', 'select', 'view', or 'exit'. ")
            self.ask_user()

    def exit_program(self):
        self.print_.print_statement("Thanks for book hunting. Happy Reading!")
        sys.exit()

    def search_for_books(self):
        keyword = self.user_input.get_search_keyword()
        searchtype = self.user_input.get_search_type()
        if searchtype == "no":
            text = "no"
        elif searchtype != "no" and not self.rules.is_searchtype_valid(searchtype):
            self.print_.print_statement("Hmm, I don't have that as a searchtype. Try again? ")
            self.search_for_books()
        else:
            text = self.user_input.get_search_text()
        data = self.book_searching.search_for_books(text, searchtype, keyword)
        book_info = self.book_searching.select_five_books(data)
        if self.rules.is_search_empty(book_info):
            self.print_.print_statement("Hmm, it looks like there weren't any results. Try again? ")
        else:
            self.print_.print_book_info(book_info)
        self.ask_user()

    def select_book(self):
        if self.rules.is_search_empty(self.book_searching.book_info):
            self.print_.print_statement("You need to perform a search before you can select a book to add to your reading list. ")
            self.ask_user()
        selected_book = self.user_input.select_a_book()
        if self.rules.is_selected_book_integer(selected_book) and self.rules.is_selected_book_in_book_info(selected_book):
            self.readingList.add_to_reading_list(selected_book, self.book_searching.book_info)
            self.print_.print_statement("Here's your current reading list: ")
            self.print_.print_reading_list(self.readingList.reading_list)
        else:
            self.print_.print_statement("Hmm, that didn't work. Please enter a number only between 1-5 to select your book.")
        self.ask_user()

    def view_reading_list(self):
        reading_list = self.readingList.reading_list
        if self.rules.is_reading_list_empty(reading_list):
            self.print_.print_statement("Looks like your reading list is empty. ")
        else:
            self.print_.print_statement("Here's your current reading list. ")
            self.print_.print_reading_list(reading_list)
        self.ask_user()


if __name__ == '__main__':
    runningprogram = RunProgram(BookSearching(), ReadingList(), UserInput(), Print(), Rules())
    runningprogram.start_program()
