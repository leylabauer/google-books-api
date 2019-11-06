import json
import requests
# from collections import Counter probably take that out.
import operator

key = 'AIzaSyCU2dyXMyOEp9rhcYonOmrhQ_ugikWyi9s'

class bookSearching:

    def __init__(self, reading_list={}):
        self.reading_list = reading_list

    def search_for_books(self, text, searchtype, keyword):
        response = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + text + '+' + searchtype + ':' + keyword + '&key=AIzaSyCU2dyXMyOEp9rhcYonOmrhQ_ugikWyi9s')
        data = json.loads(response.text)
        bookinfo = {}
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
                publisher = "No publisher listed."
            bookinfo.update({j: [title, author, publisher]})
            j += 1
        return bookinfo

    def add_selected_book_to_reading_list(self, selected_book, bookinfo):
        selected_book_to_add = bookinfo[int(selected_book)]
        book_number = len(self.reading_list) + 1
        self.reading_list.update({book_number: selected_book_to_add})

class userInput:

    def __init__(self, text="", searchtype="", keyword="" ):
        self.text = text
        self.searchtype = searchtype
        self.keyword = keyword

    def help_show_user_searchterms(self):
        print("Here are the search keywords: ")
        print("Use 'intitle' if the keyword is in the title.")
        print("Use 'inauthor' if the keyword is in the author.")
        print("Use 'inpublisher' if the keyword is in the publisher.")
        print("Use 'insubject' if the keyword is in the subject.")
        print("Use 'isbn' if you know the book's ISBN.")
        print("Use 'lccn' to get the keyword's Library of Congress control number.")
        print("Use 'oclc' to get the keyword's Online Computer Library Center number.")

    def get_search_text(self):
        text = input("Give me text to search. ")
        while text.lower() == "help":
            self.help_show_user_searchterms()
            text = input("Give me text to search. ")
        return text
        
    def get_searchtype(self):
        searchtype = input("What's the search method for this? Type it in or write 'help' for help. ")
        while searchtype.lower() == "help":
            self.help_show_user_searchterms()
            searchtype = input("What's the search method for this? Type it in or write 'help' for help. ")
        return searchtype

    def get_search_keyword(self):
        keyword = input("What's the keyword for the book you want? ")
        while keyword.lower() == "help":
            self.help_show_user_searchterms()
            keyword = input("What's the keyword for the book you want? ")
        return keyword

    def does_user_want_to_select_search_view_or_exit(self):
        answer = input("Do you want to search for a book, select a book for your reading list, view your reading list, or exit? Enter 'search', 'select', 'view', or 'exit'. ")
        return answer.lower()

    def select_a_book(self):
        selected_book = input("What book number do you want to select? ")
        return selected_book

class userInputRules:

    def __init__(self):
        pass

    def check_if_selected_book_is_int(self, selected_book):
        if type(int(selected_book)) is int:
            return True

class printToCL:

    def __init__(self):
        pass

    def print_opening_information(self):
        print(('*') * 6)
        print("Welcome to the Command Line Google Books API!")
        print("You'll be asked to enter text you'd like to search for, what kind of search method you want to use, and what keywords to look for in that text.")
        print("To see the different types of search methods, type 'help'. To exit the program, type 'exit'. ")
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
        print("Thanks! It's been added to your reading list. ")

    def print_goodbye(self):
        print("Thanks for book hunting. Happy Reading!")

class runProgram:

    def __init__(self, bookSearching, userInput, printToCL, userInputRules):
        self.bookSearching = bookSearching
        self.userInput = userInput
        self.printToCL = printToCL
        self.userInputRules = userInputRules

    def make_the_program_work(self):
        reading_list = self.bookSearching.reading_list
        self.printToCL.print_opening_information()
        select_search_or_exit = self.userInput.does_user_want_to_select_search_view_or_exit()
        while select_search_or_exit == 'search':
            text = self.userInput.get_search_text()
            searchtype = self.userInput.get_searchtype()
            keyword = self.userInput.get_search_keyword()
            bookinfo = self.bookSearching.search_for_books(text, searchtype, keyword)
            self.printToCL.print_book_info(bookinfo)
            select_search_or_exit = self.userInput.does_user_want_to_select_search_view_or_exit()
        while select_search_or_exit == 'select':
            selected_book = self.userInput.select_a_book()
            if self.userInputRules.check_if_selected_book_is_int(selected_book):
                self.bookSearching.add_selected_book_to_reading_list(selected_book, bookinfo)
                # reading_list = self.bookSearching.reading_list
                self.printToCL.print_reading_list(reading_list)
                select_search_or_exit = self.userInput.does_user_want_to_select_search_view_or_exit()
            else:
                self.printToCL.print_selected_book_is_not_int()
                select_search_or_exit = self.userInput.does_user_want_to_select_search_view_or_exit()
        while select_search_or_exit == 'view':
            self.printToCL.print_reading_list(reading_list)
            select_search_or_exit = self.userInput.does_user_want_to_select_search_view_or_exit()
        if select_search_or_exit == 'exit':
            self.printToCL.print_goodbye()


booksearch = bookSearching()
userinput = userInput()
printtocl = printToCL()
userinputrules = userInputRules()
rundammit = runProgram(booksearch, userinput, printtocl, userinputrules)
rundammit.make_the_program_work()