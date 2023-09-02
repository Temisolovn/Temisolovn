count = 0
limit = 3
is_yes = False
secret = ()
letter =()

words = {
    "a" : "Apple",
    "b" : "Ball",
    "c" : "Cat",
    "d" : "Dog",
    "e" : "Egg",
    "f" : "Fan",
    "g" : "Goat",
    "h" : "Hen",
    "i" : "Ink",
    "J" : "Jug",
    "k" : "Kite",
    "l" : "Lion",
    "m" : "Mat",
    "n" : "Note",
    "o" : "Old",
    "p" : "Pen",
    "q" : "Queen",
    "r" : "Rat",
    "s" : "Sun",
    "t" : "Tin",
    "u" : "Umbrella",
    "v" : "Van",
    "w" : "Wand",
    "x" : "X-ray",
    "y" : "Yell",
    "Z" : "Zebra"
}

description = {
    "a" : "Apple",
    "b" : "Ball",
    "c" : "Cat",
    "d" : "Dog",
    "e" : "Egg",
    "f" : "Fan",
    "g" : "Goat",
    "h" : "Hen",
    "i" : "Ink",
    "J" : "Jug",
    "k" : "Kite",
    "l" : "Lion",
    "m" : "Mat",
    "n" : "Note",
    "o" : "Old",
    "p" : "Pen",
    "q" : "Queen",
    "r" : "Rat",
    "s" : "Sun",
    "t" : "Tin",
    "u" : "Umbrella",
    "v" : "Van",
    "w" : "Wand",
    "x" : "X-ray",
    "y" : "Yell",
    "Z" : "Zebra"
}

while secret != words.get(letter) and is_yes == False:
    if count < limit:
        letter = input("Select a word to guess: ")
        print(description.get(letter))
        secret = input("Guess the word: ")
        count +=1
    else:
        is_yes = True

if secret == words.get(letter):
    print("Yes")
else:
    print("No")