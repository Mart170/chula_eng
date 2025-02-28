import tkinter as tk
import random

# List of flashcards containing Thai consonants and their names.
flashcards = [
    {"letter": "ก", "name": "gor kai"},
    {"letter": "ข", "name": "khor khai"},
    {"letter": "ค", "name": "khor khuat"},
    # Add more flashcards as needed.
]

class FlashCardGame:
    def __init__(self, master):
        self.master = master
        master.title("Thai Consonant Flashcard Game")
        
        self.current_card = None
        self.is_flipped = False

        # Label to display the flashcard content.
        self.card_label = tk.Label(master, text="", font=("Helvetica", 72))
        self.card_label.pack(pady=50)

        # Frame to hold the buttons.
        button_frame = tk.Frame(master)
        button_frame.pack(pady=20)

        # Button to flip the card.
        self.flip_button = tk.Button(button_frame, text="Flip", font=("Helvetica", 16), command=self.flip_card)
        self.flip_button.pack(side=tk.LEFT, padx=10)

        # Button to go to the next card.
        self.next_button = tk.Button(button_frame, text="Next", font=("Helvetica", 16), command=self.next_card)
        self.next_button.pack(side=tk.RIGHT, padx=10)

        self.next_card()  # Initialize the first card.

    def flip_card(self):
        """Flip the card to show the opposite side."""
        if self.current_card:
            if not self.is_flipped:
                # Show the name of the consonant.
                self.card_label.config(text=self.current_card["name"])
                self.is_flipped = True
            else:
                # Show the Thai letter.
                self.card_label.config(text=self.current_card["letter"])
                self.is_flipped = False

    def next_card(self):
        """Load a new random card and reset to the front side."""
        self.current_card = random.choice(flashcards)
        self.card_label.config(text=self.current_card["letter"])
        self.is_flipped = False

if __name__ == "__main__":
    root = tk.Tk()
    game = FlashCardGame(root)
    root.mainloop()