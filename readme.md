
# Google Books Command Line Program

**Project Description**:

This program allows users to access the Google Books API. Users can search for books using a keyword. To help specify their search, they can state if the keyword relates to a title, author, subject, or publisher, and then add an optional final second keyword. Users can also simply search for a single keyword without specificity as well.

The user is then able to browse books by the top 5 search results and can add them to a Reading List. Users can view the Reading List as well.

**Technologies**

Written in Python 3.7.3

**Running the Program**:

Run the program with the command: 

    python main.py

 in the command line.

**Prerequisites**

Builtin modules sys and json are used. The module requests version 2.21.0 is utilized as well to handle the request for JSON data. Pytest version 4.3.1 is used for testing. A requirements.txt file is also available.

To install requests, type the following in the command line:

    pip install requests

To install Pytest, type the following in the command line:

    pip install pytest

**Tests**

Tests are run with Pytest. To run the tests (first be sure that Pytest is installed), run the following on the command line:

    pytest test_main.py

**Updates**

Several critical updates have been made to the project.

1. Variables/classes/methods have been renamed to be shorter, cleaner, and clearer.
2. Tests have been added to help with the testing of receiving JSON data from Google Books, testing the info given to various methods is data that can be interpreted by the program, etc.
3. Tests can now be run without having to comment out any code in the main file.
4. Print functions have been reduced.
5. An additional class (ReadingList) to help make sure that every class/method has one function has been added.

**Author**

Built by Leyla Bauer



