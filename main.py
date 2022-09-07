from tkinter import *
import random
from PIL import Image, ImageTk

root = Tk()
root.title('Deck of Cards')
root.geometry('900x500')
root.configure(background='green')

def resize_cards(card):
    our_card_img = Image.open(card)

    our_card_resize_img = our_card_img.resize((150, 218))

    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resize_img)

    return our_card_image

def shuffle():
    suits = ['diamonds', 'clubs', 'hearts', 'spades']
    values = range(2, 15)

    global deck
    deck = []

    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')

    global dealer, player
    dealer = []
    player = []

    card = random.choice(deck)
    deck.remove(card)
    dealer.append(card)

    global dealer_image
    dealer_image = resize_cards(f'cards/{card}.png')
    dealer_label.config(image=dealer_image)

    card = random.choice(deck)
    deck.remove(card)
    player.append(card)
    player_label.config(text=card)

    global player_image
    player_image = resize_cards(f'cards/{card}.png')
    player_label.config(image=player_image)

    root.title(f'Deck of Cards - {len(deck)} Cards Left')

def deal_cards():
    try:
        card = random.choice(deck)
        deck.remove(card)
        dealer.append(card)
        global dealer_image
        dealer_image = resize_cards(f'cards/{card}.png')
        dealer_label.config(image=dealer_image)
        #dealer_label.config(text=card)

        card = random.choice(deck)
        deck.remove(card)
        player.append(card)
        global player_image
        player_image = resize_cards(f'cards/{card}.png')
        player_label.config(image=player_image)
        #player_label.config(text=card)

        root.title(f'Deck of Cards - {len(deck)} Cards Left')
    except:
        root.title(f'Deck of Cards - No Cards in Deck')

my_frame = Frame(root, bg='green')
my_frame.pack(pady=20)

dealer_frame = LabelFrame(my_frame, text='Dealer', bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text='Player', bd=0)
player_frame.grid(row=0, column=1, ipadx=20)

dealer_label = Label(dealer_frame, text='')
dealer_label.pack(pady=20)

player_label = Label(player_frame, text='')
player_label.pack(pady=20)

shuffle_button = Button(root, text='Shuffle Deck', font=('MS Gothic', 14), command=shuffle)
shuffle_button.pack(pady=20)

card_button = Button(root, text='Get Cards', font=('MS Gothic', 14), command=deal_cards)
card_button.pack(pady=20)

shuffle()


root.mainloop()