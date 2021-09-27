import random, sys
import Dictionary as di
import Players

score_1 = 0
score_2 = 0

check_players = Players.check_players
players = Players.players

if players == 2:
    player_1, player_2 = check_players(players)
elif players == 3:
    player_1, player_2, player_3 = check_players(players)
elif players == 4:
    player_1, player_2, player_3, player_4 = check_players(players)

v1 = [6, 7, 8, 9, 1, 'V', 'D', 'K', 'T']
s1 = ['_♦️', '_♠️', '_♥️', '_♣️']
table= []
score = []
max_score = 220


# Deck of 36 cards
def deck(arr1, arr2):
    arr4 = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            arr3 = ['%s' % arr1[i] + '%s' % arr2[j]]
            arr4 += arr3
    return arr4
deck = list(deck(v1, s1))


# shuffle deck
def shuffle_deck():
    random.shuffle(deck)
    return deck


# Returns the last placed card to the table
def show_table(): 
    if len(table) > 1:
        table_end = table[-1]
        return table_end
    elif len(table) == 1:
        table_end = table[0]
        return table_end
    elif len(table) < 1:
        table_end = deck.pop(-1)
        table.append(table_end)
        return table_end


# deal of five cards
def deal_cards(p):
    for i in range(0,5):
        if len(p) <= 4:
            p.append(deck.pop(i))
            p.sort()
        elif len(p) == 5:
            break
    return(p)


# Get the map index
def iter_l(p, index):
    try:
        x = p.index(index)
        c = p[x]
        return c
    except:
        "error"


# Returns a card from the table list
def table_card(p, index):
    x = p.index(index)
    table.append(p.pop(x))
    return table


# Checking the card for convergence by suit or sign
# We make a move
def move_card(p):
    print("\nYour cards:", p)
    while True:
        index = input("Choose card:")
        if index == "stop":
            sys.exit()
        else:
            try:
                table_end = show_table()
                print("On table:", table_end)
                t_suit = table_end[1:]
                t_num = table_end[:1]
                c = iter_l(p, index)
                p_suit = c[1:]
                p_num = c[:1]
                if t_suit == p_suit:
                    table_card(p, index)
                    break
                elif t_suit != p_suit:
                    if t_num == p_num:
                        table_card(p, index)
                        break
                    elif t_num != p_num:
                        if p_num == "V":
                            table_card(p, index)
                            break
                        else:
                            print("\nChoose another card")
                            continue
            except:
                print("\nNo card found please try again")
                continue


# We take a card from the deck
def take_card(p):
    print("Your cards:", p)
    try:
        one_card = deck.pop(0)
        p.append(one_card)
    except:
        while table:
            deck.append(table[0])
            del table[0]
        one_card = deck.pop(0)
        p.append(one_card)
    return p


# Checking Player Cards Using a Dictionary
def iteration_count(p, score):
    count = di.count
    n = []
    for i in range(len(p)):
        n += [count.setdefault(p[i])]
    for i in range(len(n)):
        score += n[i]
    return score


# Check for max score
def max_score_p(score):
    if score == max_score:
        score = (score*0)
        return score
    elif score >= max_score:
        sys.exit()
    else:
        pass


def move_p1(p):
    table.append(p.pop(0))
    return p

# Stop the game
def stop():
    sys.exit()


def help():
    print("\n1. Choose an action:",
    "\n2. To select a map - 'move' (action)",
    "\n3. To walk like a map - '6_♦' (After a move action)",
    "\n2. To take a card - 'take' (action)",
    "\n3. To skip a move - 'check' (action)",
    "\n4. To stop the game - 'stop' (action)")

# Player check for the end of cards
def check_p(p1, p2):
    global score_1
    global score_2
    while True:
        if len(p1) < 1:
            if len(p2) > 1:

                score_2 =+ iteration_count(p2, score_2)
                
                if score_2 == max_score:
                    score_2 = (score_2 * 0)
                    print("Score player 1:", score_1)
                    print("Score player 2:", score_2)
                elif score_2 >= max_score:
                    print("Player 2 lost")
                    print("Score player 1:", score_1)
                    print("Score player 2:", score_2)
                    sys.exit()
                elif score_2 <= max_score:
                    print("Score player 1:", score_1)
                    print("Score player 2:", score_2)
                
                while table:
                    deck.append(table[0])
                    del table[0]
                while p2:
                    deck.append(p2[0])
                    del p2[0]

                s = input("Start game again Y or N:")
                if s == "Y":
                    start_game()
                elif s == "N":
                    sys.exit()
        if len(p2) < 1:
            if len(p1) > 1:
                
                score_1 =+ iteration_count(p1, score_1)

                if score_1 == max_score:
                    score_1 = (score_1 * 0)
                    print("Score player 1:", score_1)
                    print("Score player 2:", score_2)
                elif score_1 >= max_score:
                    print("Player 1 lost")
                    print("Score player 1:", score_1)
                    print("Score player 2:", score_2)
                    sys.exit()
                elif score_1 <= max_score:
                    print("Score player 1:", score_1)
                    print("Score player 2:", score_2)

                while table:
                    deck.append(table[0])
                    del table[0]
                while p1:
                    deck.append(p1[0])
                    del p1[0]

                s = input("Начать игру снова Y or N:")
                if s == "Y":
                    start_game()
                elif s == "N":
                    sys.exit()
        else:
            break

# integrates all functions
def all_move(p):
    while True:
        print("Your cards:", p)
        print("On the table:", show_table())
        s = input("Choose an action:")
        if s == "take":
            take_card(p)
            while True:
                print("On the table:", show_table())
                print("Your cards:", p)
                s = input("Select action 'check' or 'move':")
                if s == "check":
                    break
                elif s == "move":
                    print("On the table:", show_table())
                    move_card(p)
                    break
            break
        elif s == "help":
            help()
            continue
        elif s == "move":
            print("On the table:", show_table())
            move_card(p)
            break
        elif s == "stop":
            stop()


def beginning_game():
    shuffle_deck()
    deal_cards(player_1)
    move_p1(player_1)
    deal_cards(player_2)

    print("Количество карт: " + "%s" % len(deck),
    "\nИгрок 1:", player_1,
    "\nХод: " + "%s" % show_table(), 
    "\nИгрок 2:", player_2)

def start_game():
    beginning_game()
    while True:

        print("\nХод игрока 2")
        all_move(player_2)
        print("На столе:", show_table())

        check_p(player_1, player_2)

        print("\nХод игрока 1")
        all_move(player_1)
        print("На столе:", show_table())
        
        check_p(player_1, player_2)


start_game()
