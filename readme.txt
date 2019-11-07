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


1. be sure to activate the google api you want to use
that is attached to your account/the api key. i did not do
this at first so it didn't work at first. 

in building this project:

1. created a conda environment, google_books_env



Edge cases to solve for:
if the user enters a keyword that doesn't work


Trying to fix a logic error and separating out how to select a book and add it to the reading list. 
But, the book info is only being saved in the one method from searching so I can't access it. Should
I have it as a variable used in that entire object then, maybe?
YES THAT WAS THE ANSWER BITCH. HOLY FUCK.

somethign that has no results:
fart
insubjecct
fartbox


Left off trying to fix the select so that if you try to select when you don't have a search performed it tells you no.
This works but hten when you try to quit the program later it yells at you for having no way to select with the empty
bookinfo dict that results from the search.

Still need to:
1. Add in tests.
2. Add in command not found for the searchtype option.
3. Fix the double exit typing thing (that's weird)
