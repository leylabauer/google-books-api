import json
import requests
import sys

key = 'AIzaSyCU2dyXMyOEp9rhcYonOmrhQ_ugikWyi9s'

class bookSearching:

    def __init__(self, reading_list={}, bookinfo = {}):
        self.reading_list = reading_list
        self.bookinfo = bookinfo

    def search_for_books(self, text, searchtype, keyword):
        if searchtype == "no":
            response = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + keyword + '&key=AIzaSyCU2dyXMyOEp9rhcYonOmrhQ_ugikWyi9s')
            data = json.loads(response.text)
        elif text == "no":
            response = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + searchtype + ':' + keyword + '&key=AIzaSyCU2dyXMyOEp9rhcYonOmrhQ_ugikWyi9s')
            data = json.loads(response.text)
        else: 
            response = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + text + '+' + searchtype + ':' + keyword + '&key=AIzaSyCU2dyXMyOEp9rhcYonOmrhQ_ugikWyi9s')
            data = json.loads(response.text)
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
            self.bookinfo.update({j: [title, author, publisher]})
            j += 1
        return self.bookinfo

    def add_selected_book_to_reading_list(self, selected_book, bookinfo):
        selected_book_to_add = self.bookinfo[int(selected_book)]
        book_number = len(self.reading_list) + 1
        self.reading_list.update({book_number: selected_book_to_add})

class userInput:

    def __init__(self, text="", searchtype="", keyword="" ):
        self.text = text
        self.searchtype = searchtype
        self.keyword = keyword

    def get_search_text(self):
        text = input("Is there an additional keyword to help with your search? If not, enter 'no'. ")
        return text.lower()
        
    def get_searchtype(self):
        searchtype = input("Is this keyword related to the author, the subject, the title, or the publisher? Enter 'inauthor', 'insubject', 'intitle', 'inpublisher', or 'no'. ")
        return searchtype.lower()

    def get_search_keyword(self):
        keyword = input("What keyword do you want to look up? ")
        return keyword.lower()

    def does_user_want_to_select_search_view_or_exit(self):
        answer = input("Do you want to search for a book, select a book from a search to add to your reading list, view your reading list, or exit? Enter 'search', 'select', 'view', or 'exit'. ")
        return answer.lower()

    def select_a_book(self):
        selected_book = input("What book number do you want to select? ")
        return selected_book

class userInputRules:

    def __init__(self):
        pass

    def check_if_selected_book_is_int(self, selected_book):
        try:
            if type(int(selected_book)) is int:
             return True
        except ValueError:
            return False

    def check_if_search_is_empty(self, bookinfo):
        if len(bookinfo) == 0:
            return True
        elif bookinfo[1] == ["No title listed", "No authors listed", "No publisher listed"]:
            return True
        else:
            return False

    def check_if_searchtype_input_is_accurate(self, searchtype):
        if searchtype in ['inauthor', 'insubject', 'intitle', 'inpublisher']:
            return True
        else:
            return False

class printToCL:

    def __init__(self):
        pass

    def print_opening_information(self):
        print(('*') * 6)
        print("Welcome to the Command Line Google Books API!")
        print("To exit the program, type 'exit'. ")
        print(('*') * 6)

    def print_book_info(self, bookinfo):
        j = 1
        for item in bookinfo:
            print('Book #' + str(j) + ':')
            print('Title: ' + bookinfo[j][0])
            print('Author(s): ')
            if type(bookinfo[j][1]) == list:
                for auth in bookinfo[j][1]:
                    print(auth)
            else:
                print(bookinfo[j][1])
            print('Publisher: ' + bookinfo[j][2])
            print("***")
            j += 1

    def print_reading_list(self, reading_list):
        if len(reading_list) > 0:
            j = 1
            print(('*') * 6)
            print("Here's your current reading list: ")
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
        else:
            print("Looks like your reading list is empty. ")

    def print_selected_book_is_not_int(self):
        print("Hmm, that didn't work. Please enter only the number of the book you want to select.")

    def print_added_to_reading_list(self):
        print("Great! It's been added to your reading list. ")

    def print_no_results_found(self):
        print("Hmm, it looks like there weren't any results. Try again? ")

    def print_unknown_command(self):
        print("Hmm, I don't have that option. Please enter 'search', 'select', 'view', or 'exit'. ")

    def print_unknown_search_command(self):
        print("Hmm, I don't have that option. Try again? ")

    def print_perform_search_first(self):
        print("You need to perform a search before you can select a book to add to your reading list. ")

    def print_goodbye(self):
        print("Thanks for book hunting. Happy Reading!")

class runProgram:

    def __init__(self, bookSearching, userInput, printToCL, userInputRules):
        self.bookSearching = bookSearching
        self.userInput = userInput
        self.printToCL = printToCL
        self.userInputRules = userInputRules

    def starting_program(self):
        self.printToCL.print_opening_information()
        self.make_the_program_work()

    def make_the_program_work(self):
        select_search_or_exit = self.userInput.does_user_want_to_select_search_view_or_exit()
        if select_search_or_exit == 'search':
            self.searching_for_books()
        elif select_search_or_exit == 'exit':
            self.exit_program()
        elif select_search_or_exit == 'select':
            self.select_book()
        elif select_search_or_exit == 'view':
            self.view_reading_list()
        else:
            self.printToCL.print_unknown_command()
            self.make_the_program_work()

    def exit_program(self):
        self.printToCL.print_goodbye()
        sys.exit()

    def searching_for_books(self):
        keyword = self.userInput.get_search_keyword()
        searchtype = self.userInput.get_searchtype()
        if searchtype == "no":
            text = "no"
        elif searchtype != "no" and not self.userInputRules.check_if_searchtype_input_is_accurate(searchtype):
            self.printToCL.print_unknown_search_command()
            self.searching_for_books()
        else:
            text = self.userInput.get_search_text()
        bookinfo = self.bookSearching.search_for_books(text, searchtype, keyword)
        if self.userInputRules.check_if_search_is_empty(bookinfo):
            self.printToCL.print_no_results_found()
            self.make_the_program_work()
        self.printToCL.print_book_info(bookinfo)
        self.make_the_program_work()

    def select_book(self):
        if self.userInputRules.check_if_search_is_empty(self.bookSearching.bookinfo):
            self.printToCL.print_perform_search_first()
            self.make_the_program_work()
        selected_book = self.userInput.select_a_book()
        if self.userInputRules.check_if_selected_book_is_int(selected_book):
            self.bookSearching.add_selected_book_to_reading_list(selected_book, self.bookSearching.bookinfo)
            reading_list = self.bookSearching.reading_list
            self.printToCL.print_reading_list(reading_list)
            self.make_the_program_work()
        else:
            self.printToCL.print_selected_book_is_not_int()
            self.make_the_program_work()

    def view_reading_list(self):
        reading_list = self.bookSearching.reading_list
        self.printToCL.print_reading_list(reading_list)
        self.make_the_program_work()


# To run the tests, comment out the code below.

booksearch = bookSearching()
userinput = userInput()
printtocl = printToCL()
userinputrules = userInputRules()
runningprogram = runProgram(booksearch, userinput, printtocl, userinputrules)
runningprogram.starting_program()
