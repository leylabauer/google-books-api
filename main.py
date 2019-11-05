import json
import requests
from collections import Counter
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
        for i in range(5):
            try: 
                books.append(data["items"][i]["volumeInfo"]["title"])
            except:
                books.append("No title listed")
            try:
                authors.append(data["items"][i]["volumeInfo"]["authors"])
            except:
                authors.append("No authors listed")
            try: 
                publisher = data["items"][i]["volumeInfo"]["publisher"]
                publishers.append(publisher)
            except:
                publishers.append("No publisher listed.")
        bookinfo = list(zip(books, authors, publishers))
        return bookinfo

    def books_as_tuples_in_list(self, books, authors, publishers):
        pass
        

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

class printToCL:

    def __init__(self):
        pass

    def print_book_info(self, bookinfo):
        i = 1
        for item in bookinfo:
            print("Info on Book #"+ str(i) +": ")
            print(item)
            i = i + 1


class runProgram:

    def __init__(self, bookSearching, userInput, printToCL):
        self.bookSearching = bookSearching
        self.userInput = userInput
        self.printToCL = printToCL

    def make_the_program_work(self):
        text = self.userInput.get_search_text()
        searchtype = self.userInput.get_searchtype()
        keyword = self.userInput.get_search_keyword()
        bookinfo = self.bookSearching.search_for_books(text, searchtype, keyword)
        # bookinfo = self.bookSearching.books_as_tuples_in_list()
        print(bookinfo)
        self.printToCL.print_book_info(bookinfo)

booksearch = bookSearching()
userinput = userInput()
printtocl = printToCL()
rundammit = runProgram(booksearch, userinput, printtocl)
rundammit.make_the_program_work()