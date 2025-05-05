 Script Grabber: ISBN Book Info Fetcher
This Python script automates the process of retrieving book data using random ISBNs. It selects an ISBN from a local list, queries the Open Library API for metadata (e.g., title, author), and writes the result to file.txt. If a book isn’t found or the API request fails, the script gracefully handles the error with a message.

Simple, lightweight, and hands-free—just run the script to generate a file of book data from real-world sources.




Script          grabber          External API          writer
  |                |                  |                  |
  |                |                  |                  |
  |--- random_isbn -->                |                  |
  |                |                  |                  |
  |                |--- API request ------>              |
  |                |                  |                  |
  |                |<-- API response ---                 |
  |                |                  |                  |
  |<-- book data/None ---             |                  |
  |                |                  |                  |
  |--- book data ------>              |                  |
  |                |                  |                  |
  |                |                  |--- Write to file.txt
  |                |                  |                  |
  |                |                  |                  |
