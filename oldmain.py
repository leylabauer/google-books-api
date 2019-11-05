# // 1. Type in a query and display a list of 5 books matching that query
# // (and you might have to reset maxResults to be 5 instead
# // of the default 10)
# // 2. Each item in the list should include the book's author, title, 
# // and publishing company.
# // 3. A user should be able to select a book from the five displayed
# // to save to a 'Reading List'
# // 4. View a 'Reading List' with all the books the user has 
# // selected from their queries -- this is local
# // and not tied to Google Book's account features. 

# // Step 1. Type a query into the CL and get it to return.

if __name__ == '__main__':

    import json
    import requests
    from collections import Counter
    import operator

    key = 'AIzaSyCU2dyXMyOEp9rhcYonOmrhQ_ugikWyi9s'

class Books:

    def __init__(self):
        pass
    
    def help_show_user_searchterms(self):
        print("hello")

    def search_for_books(self):
        # Allows for users to search for a book
        text = input("Give me text to search. ")
        searchtype = input("What's the search method for this? Type it in or write 'help' for help. ")
        while searchtype.lower() == "help":
            help_show_user_searchterms()
            searchtype = input("What's the search method for this? Type it in or write 'help' for help. ")
        keyword = input("What's the keyword for the book you want? ")
    
    # def print_book_results(self, text=""):
    #     self.text = search_for_books.text
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
        print(books)
        print(authors)
        print(publishers)

book = Books()
book.search_for_books()
# book.print_book_results()


# $.get('https://www.googleapis.com/books/v1/volumes?q=' + text + '+' + searchtype + ':' + keyword + '&key=AIzaSyCU2dyXMyOEp9rhcYonOmrhQ_ugikWyi9s', function(data) {
#     console.log(data)
# })}






# // The reading list needs a specific number above 1000,
# // so let's have the reading list be 1001.