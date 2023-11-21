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

ok so this script is pretty basic it just grabs book details using isbn numbers first it picks a random isbn from a list we got then it sends this isbn to some api at openlibrary.org to get the book info like title and author and stuff if it works it writes this info into a file called file.txt but if it doesnt get the info or something goes wrong it just prints out an error message you just run the script and it does all this by itself thats pretty much all it does nothing too fancy.