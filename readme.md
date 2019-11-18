
# Google Books Command Line API
*by Leyla Bauer*


**Project Description**:

This program allows users to access the Google Books API. Users can search for books using a keyword. To help specify their search, they can state if the keyword relates to a title, author, subject, or publisher, and then add an optional final second keyword. Users can also simply search for a keyword without specificity as well.

The user is then able to browse books by the top 5 search results and can add them to a Reading List. Users can view the Reading List as well.

**Running the Program**:

Run the program with the command python main.py in the command line.

**Code Description**:

This project is built in Python3 using OOP. Imported Python libraries include json, requests, and sys to assist in reading the JSON info from Google Books and with exiting the program.

There are 5 classes that work together to run the program.

a. **class bookSearching** handles reaching out to Google Books with the search request. It recieves the requested data and takes the title, author(s), and publisher of the first 5 results and puts it into a dictionary called bookinfo. The keys in this dictionary are the book numbers (1-5), and the values are lists containing the book's title, author(s), and publisher. If the data does not have a result for title, publisher and/or author(s), an automatic value of 'No xxx listed' is added in its place. If a user wants to add a book to their reading list, this class can also take the number of the selected book and add its information to the reading_list dictionary.

b. **class userInput** handles all requests to the user for information. It has 3 methods to be able to get the keyword, the searchtype, and the text(i.e. the second additional and optional keyword) from the user. All input from the user is automatically switched to lowercase for use later in the program.
Additional methods from this include asking the user if they want to search for a book, select a book for their reading list, view their reading list, or exit. The last method is called if a user chooses to select a book from their reading list, and it asked for an integer input of the number of the book they want to add to their reading list.

c. **class userInputRules**: performs checks to make sure the input from the user is accurate to run the rest of the program. There are two methods that deal with the user's input in selecting a book from the bookinfo dictionary, one which makes sure the info is an integer and one which makes sure the integer is between 1-5 (the only options available to the user).
Another method checks to see if the search results are empty. It does this by either seeing if the length of the bookinfo dictionary is 0, or if the first book's values for title, author(s), and publisher are all 'No xxx listed'. 
The final method checks if the searchtype input given by the user matches the available search methods.

d. **class printToCl**: handles all print statements that go to the command line and to the user. It handles showing error messages and also displaying the information from both the bookinfo and reading_list dictionaries.

e. **class runProgram**: is the class which runs the entire program. It contains a starting_program method which calls upon the opening print instructions and the main method for the entire application, the make_the_program_work() method.

1. **make_the_program_work()** contains the main information for the user, and asks them if they want to search, select, view their reading list, or exit the program. If a command entered does not match one of these commands, the method prints an error and calls on itself again until an accurate command is entered.

2. **exit_program()** is a method that prints an exit statement and quits the entire program.

3. **searching_for_books()** is a method that gets the mandatory keyword and optional searchtype and optional secondary keyword (known as the variable text) from the user. If a given searchtype is not accurate, the method prints an error statement and calls upon the make_the_program_work() method to start the process over. If the user enters a keyword but enters the command 'no' for a searchtype, the method immediately searches for and displays the bookinfo for the given search. If the user doesn't define a secondary keyword, it bypasses that option and displays the bookinfo for the given search.

4. **select_book()** handles the logic for selecting a book and adding it to the user's reading_list. It checks if the user's selection is an integer and if it's in the range of 1-5 (the number of books displayed from the search). If those fail, it defaults back to the make_the_program_work() method. If they succeed, it takes the selected book, adds it to the reading_list, and prints it to the user.

5. **view_reading_list()** displays the user's reading_list by calling on the printToCl.print_reading_list() function. If the reading_list is empty, the print_reading_list() function will print a failure statement. After this the make_the_program_work() function is called.


**Tests**

Several tests have been included, created and tested with pytest. This is a section which can be expanded upon in the future. To run the tests as given, the code at the bottom of main.py which instantiates the objects and starts the program must be commented out. A comment in the main.py code itself shows where the code must be commented out to run the tests.

**Future updates, revisions, and comments**:

I tried to make this code simple to follow but with ample handling of edge cases. It is longer than I expected it to be, but I think relatively effective. There was originally a help function with the code which I took out of the final submitted version after simplifying the instructions and attempting to take out anything that might confuse the user. 

A few things were intentionally left out, such as a user being able to exit the program in the middle of a search. I did not add this in to allow for a user to search for a book with the keyword 'exit'.

For future verions of the code, I would look to simplifying it a bit if I can and expanding on the tests for it. I did not include any tests for faking input, hence having to comment out the code that instantiates the objects in order for the tests to run. In the future I would like to try to add this in; it was left out in this version due to time constraints. I would also like to redo and simplify some of the print statements, especially the print_reading_list() method because I think it would be better to take out that second functionality of making sure the reading list isn't empty, and putting another method to check that in the userInputRules class. This is another thing that has been left out due to time constraints. 

# Thank you for reading and I look forward to feedback!
