import json
import requests
# from collections import Counter probably take that out.
import operator

key = 'AIzaSyCU2dyXMyOEp9rhcYonOmrhQ_ugikWyi9s'

class bookSearching:

    def __init__(self):
        pass

    def search_for_books(self, text, searchtype, keyword):
        response = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + text + '+' + searchtype + ':' + keyword + '&key=AIzaSyCU2dyXMyOEp9rhcYonOmrhQ_ugikWyi9s')
        data = json.loads(response.text)
        books = []
        authors = []
        publishers = []
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
        # bookinfo = list(zip(books, authors, publishers))
        return bookinfo

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
        return text
        
    def get_searchtype(self):
        searchtype = input("What's the search method for this? Type it in or write 'help' for help. ")
        while searchtype.lower() == "help":
            self.help_show_user_searchterms()
            searchtype = input("What's the search method for this? Type it in or write 'help' for help. ")
        return searchtype

    def get_search_keyword(self):
        keyword = input("What's the keyword for the book you want? ")
        return keyword

    def does_user_want_to_select_or_search(self):
        answer = input("Do you want to search again or select a book for your reading list?\
            Type the book number to select a book or type 'search' to search again.")
        return answer

    def select_a_book(self):
        selected_book = input("What book number do you want to select?")
        # if selected_book:

class userInputRules:

    def __init__(self):
        pass

    # def is_user_selection_a_number(self, selected_book):
    #     return if type(selected_book) is int

class printToCL:

    def __init__(self):
        pass

    def print_book_info(self, bookinfo):
        # print(bookinfo[1][1])
        j = 1
        for item in bookinfo:
            print('Book #' + str(j) + ':')
            print(bookinfo[j][0])
            print('Author: ')
            for auth in bookinfo[j][1]:
                print(auth)
            print('Publisher: ' + bookinfo[j][2])
            j += 1

class runProgram:

    def __init__(self, bookSearching, userInput, printToCL, userInputRules):
        self.bookSearching = bookSearching
        self.userInput = userInput
        self.printToCL = printToCL
        self.userInputRules = userInputRules

    def make_the_program_work(self):
        text = self.userInput.get_search_text()
        searchtype = self.userInput.get_searchtype()
        keyword = self.userInput.get_search_keyword()
        bookinfo = self.bookSearching.search_for_books(text, searchtype, keyword)
        self.printToCL.print_book_info(bookinfo)
        self.userInput.does_user_want_to_select_or_search()

booksearch = bookSearching()
userinput = userInput()
printtocl = printToCL()
userinputrules = userInputRules()
rundammit = runProgram(booksearch, userinput, printtocl, userinputrules)
rundammit.make_the_program_work()