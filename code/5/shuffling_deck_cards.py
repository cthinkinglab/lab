from random import randrange

def create_deck():
    cards = []
    for suit in ["s", "h", "d", "c"]:
        for value in list(range(2,10)) + ["T", "J", "Q", "K", "A"]:
            # Construct the card and add it to the list
            cards.append(value + suit)
    return cards


def shuffle(cards):
    for i in range(len(cards)):
        # Pick a random index between the current index and the end of the list
        other_pos = randrange(i, len(cards))
        
        tmp = cards[i]
        cards[i] = cards[other_pos]
        cards[other_pos] = tmp


def main():
    cards = create_deck()
    print(f"The original deck of cards is: \n{cards}\n")
    
    shuffle(cards)
    print(f"The shuffled deck of cards is: \n{cards}\n")
    

# Call the main function only if this code has not been imported into another program
if __name__ == "__main__":
    main()
