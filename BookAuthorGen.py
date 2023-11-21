import requests
import random


ISBN = [

    "9780141182346",
    "9780345329455",  # At the Mountains of Madness
    "9781530338556",  # The Shadow over Innsmouth
    "9780451457998",  # Arthur C. Clarke - 2001: A Space Odyssey
    "9780345404473",  # Philip K. Dick - Do Androids Dream of Electric Sheep?
    "9781451673319",  # Ray Bradbury - Fahrenheit 451
    "9780441788385",
    "9780553293357",  # Isaac Asimov - Foundation
    "9780553213386",  # H.G. Wells - The War of the Worlds
    "9780141391657",  # Jules Verne - Twenty Thousand Leagues Under the Sea
    "9780441478125",  # Ursula K. Le Guin - The Left Hand of Darkness
    "9780553380958",  # Neal Stephenson - Snow Crash
    "9780441172719",  # Frank Herbert - Dune
    "9780312863555",  # George R.R. Martin - A Game of Thrones
    "9780316033671",  # Stephenie Meyer - Twilight
    "9780261103573",  # J.R.R. Tolkien - The Lord of the Rings
    "9780545010221",  # J.K. Rowling - Harry Potter and the Deathly Hallows
    "9780441569595",  # William Gibson - Neuromancer
    "9780451524935",  # Orson Scott Card - Ender's Game
    "9780345339683",  # George Lucas - Star Wars: From the Adventures of Luke Skywalker
    "9780765311788",  # Brandon Sanderson - Mistborn: The Final Empire
    "9780345453747",  # Dan Simmons - Hyperion
    "9780553573428",  # George R.R. Martin - A Clash of Kings
    "9780553579901",  # George R.R. Martin - A Storm of Swords
    "9780553582024",  # George R.R. Martin - A Feast for Crows
    "9780553801477",  # George R.R. Martin - A Dance with Dragons
    "9780380977270",  # Terry Pratchett - The Colour of Magic
    "9780547928227",  # J.R.R. Tolkien - The Hobbit
    "9780380789016",  # Terry Pratchett - Guards! Guards!
    "9780756404741",  # Patrick Rothfuss - The Name of the Wind
    "9780553588484",  # Robert Jordan - The Eye of the World
    "9780765365279",  # Brandon Sanderson - The Way of Kings
    "9780312890174",  # Octavia Butler - Parable of the Sower
    "9780441013593",  # Ann Leckie - Ancillary Justice
    "9780765350374",  # Jim Butcher - Storm Front
    "9780765319234",  # Peter V. Brett - The Warded Man
    "9780553106633",  # George R.R. Martin - Tuf Voyaging
    "9780316074315",  # Stephenie Meyer - The Host
    "9780553103540",  # George R.R. Martin - Fevre Dream
    "9780553382563",  # Dan Simmons - The Terror
    "9780316219368",  # James S.A. Corey - Leviathan Wakes
    "9780765336460",  # Mary Robinette Kowal - The Calculating Stars
    "9780765376466",  # Brian Staveley - The Emperor's Blades
    "9780312890723",  # Octavia Butler - Kindred
    "9780441007318",  # Roger Zelazny - Lord of Light
    "9780765364884",  # Brandon Sanderson - Warbreaker
    "9780765348273",
    "9780553382570", # Dan Simmons, Ilium
    "9780441020671", # Arthur C. Clarke, Childhood's End
    "9780345313157", # Philip K. Dick, A Scanner Darkly
    "9781451638486", # Ray Bradbury, The Martian Chronicles
    "9780451462077", # Robert A. Heinlein, Starship Troopers
    "9780553803709", # Isaac Asimov, Second Foundation
    "9780451528551", # H.G. Wells, The Time Machine
    "9780141321035", # Jules Verne, Journey to the Center of the Earth
    "9780441007318", # Ursula K. Le Guin, The Dispossessed
    "9780765345043", # Neal Stephenson, Cryptonomicon
    "9780812550702", # Frank Herbert, Children of Dune
    "9780345497468", # George R.R. Martin, A Dance with Dragons (part 2)
    "9780312983271", # Terry Pratchett, Wyrd Sisters
    "9780345418913", # Patrick Rothfuss, The Wise Man's Fear
    "9780553574746", # Robert Jordan, The Great Hunt
    "9780316194740", # Brandon Sanderson, Words of Radiance
    "9780765311788", # Octavia Butler, Kindred
    "9780316398809", # Ann Leckie, Ancillary Sword
    "9780765379887", # Jim Butcher, Fool Moon
    "9780451461278", # Peter V. Brett, The Desert Spear
    "9780553283686", # George R.R. Martin, Nightflyers
    "9780316077057", # Stephenie Meyer, Breaking Dawn
    "9780553560718", # George R.R. Martin, The Armageddon Rag
    "9780553280418", # George R.R. Martin, Windhaven
    "9780316330312", # James S.A. Corey, Caliban's War
    "9780765325037", # Mary Robinette Kowal, The Fated Sky
    "9780765366161", # Brian Staveley, The Providence of Fire
    "9780765310422", # Roger Zelazny, A Night in the Lonesome October
    "9780451464781", # Brandon Sanderson, Shadows of Self
    "9780439554930",  # J.K. Rowling - Harry Potter and the Sorcerer's Stone
    "9780439064866",  # J.K. Rowling - Harry Potter and the Chamber of Secrets
    "9780439136358",  # J.K. Rowling - Harry Potter and the Prisoner of Azkaban
    "9780439139595",  # J.K. Rowling - Harry Potter and the Goblet of Fire
    "9780439358064",  # J.K. Rowling - Harry Potter and the Order of the Phoenix
    "9780439785969",  # J.K. Rowling - Harry Potter and the Half-Blood Prince
    "9781408855652",  # J.K. Rowling - Harry Potter and the Deathly Hallows
    "9780140328721",  # Roald Dahl - Matilda
    "9780061124952",  # Harper Lee - To Kill a Mockingbird
    "9780747532743",  # J.K. Rowling - Harry Potter and the Philosopher's Stone
    "9780679826689",  # Mary Pope Osborne - Magic Tree House #1: Dinosaurs Before Dark
    "9780375813658",  # Dr. Seuss - Green Eggs and Ham
    "9780375831003",  # Dr. Seuss - The Cat in the Hat
    "9780142403877",  # E.B. White - Charlotte's Web
    "9780060256654",  # Shel Silverstein - The Giving Tree
    "9780375869021",  # Suzanne Collins - The Hunger Games
    "9780439023527",  # Suzanne Collins - Catching Fire
    "9780439023510",  # Suzanne Collins - Mockingjay
    "9780142410318",  # Jeff Kinney - Diary of a Wimpy Kid
    "9780590353403",  # J.K. Rowling - Harry Potter and the Sorcerer's Stone
    "9780064400558",  # C.S. Lewis - The Lion, the Witch, and the Wardrobe
    "9780142424179",  # Rick Riordan - The Lightning Thief
    "9780062024039",  # Veronica Roth - Divergent
    "9780399557385",  # Madeleine L'Engle - A Wrinkle in Time
    "9780142419403",  # Pseudonymous Bosch - The Name of this Book Is Secret
    "9780385732550",  # Lois Lowry - The Giver
    "9780439023480",  # Suzanne Collins - The Hunger Games
    "9780545010221",  # J.K. Rowling - Harry Potter and the Deathly Hallows
    "9780439784542",  # J.K. Rowling - Harry Potter and the Half-Blood Prince
    "9780439358071",  # J.K. Rowling - Harry Potter and the Order of the Phoenix
    "9780439139601",  # J.K. Rowling - Harry Potter and the Goblet of Fire
    "9780439136365",  # J.K. Rowling - Harry Potter and the Prisoner of Azkaban
    "9780439064873",  # J.K. Rowling - Harry Potter and the Chamber of Secrets
    "9780439708180",  # J.K. Rowling - Harry Potter and the Sorcerer's Stone
    "9780545582889",  # J.K. Rowling - Harry Potter and the Philosopher's Stone
    "9780439139595",  # J.K. Rowling - Harry Potter and the Goblet of Fire
    "9780439064873",  # J.K. Rowling - Harry Potter and the Chamber of Secrets
    "9780439136365",
    ]

def writer(book):
    with open("file.txt", "w") as file:
        file.write(f"Book: {book['title']}\n")
        file.write(f"Author: {book['author']}\n")
def grabber(isbn):
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    response = requests.get(url)
    print(f"Fetching details for ISBN: {isbn}")
    if response.status_code == 200 and response.json():
        book_data = response.json().get(f"ISBN:{isbn}", {})
        print(f"Book!: {book_data}")
        return {
            "title": book_data.get("title", "No Title Available"),
            "author": book_data.get("authors", [{}])[0].get("name", "Unknown Author")
        }
    else:
        print(f"Failed to fetch: {isbn}, Response: {response.status_code}, {response.text}")  # Log failure
        return None

random_isbn = random.choice(ISBN)
book = grabber(random_isbn)
if book:
    writer(book)
else:
    print("Failed to fetch book details")

