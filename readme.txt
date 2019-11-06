1. be sure to activate the google api you want to use
that is attached to your account/the api key. i did not do
this at first so it didn't work at first. 

in building this project:

1. created a conda environment, google_books_env

You left off trying to get the user to select a book. YOu'll have to re-do how 
you're grabbing and organizing the book info cause it's kinda confusing.
But, you'll want to add that and have the user select a book by number.
Then, that number can be added to the bookshelf called ReadingList.
The user will then have to be able to view the ReadingList
From there, add in yer tests!

You need to figure out how to better organize the info, so that the info
for each book is listed separately on a separate line. I'm not sure how to do
that, however. 
Then, you need to be sure the person can grab a book and put in on a 
reading list.

Edge cases to solve for:
if the user enters a keyword that doesn't work
if the user wants to quit
