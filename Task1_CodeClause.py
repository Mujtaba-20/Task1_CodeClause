import tkinter as tk
from tkinter import messagebox
import random

MAX_ATTEMPTS = 3

class GuessingGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("420x320")
        self.root.resizable(False, False)

        self.reset_game()
        self.build_ui()

    def reset_game(self):
        self.secret = random.randint(1, 99)
        self.attempts = 0

    def build_ui(self):
        self.title_label = tk.Label(
            self.root,
            text="Number Guessing Game\nYour instincts vs my randomness",
            font=("Arial", 13, "bold"),
            pady=15
        )
        self.title_label.pack()

        self.info_label = tk.Label(
            self.root,
            text="Guess a number between 1 and 99",
            font=("Arial", 10)
        )
        self.info_label.pack()

        self.entry = tk.Entry(self.root, font=("Arial", 12), justify="center")
        self.entry.pack(pady=10)
        self.entry.focus()

        self.submit_btn = tk.Button(
            self.root,
            text="Check Guess",
            width=15,
            command=self.check_guess
        )
        self.submit_btn.pack(pady=5)

        self.feedback_label = tk.Label(
            self.root,
            text="Attempts left: 3",
            font=("Arial", 10),
            fg="blue"
        )
        self.feedback_label.pack(pady=10)

        self.restart_btn = tk.Button(
            self.root,
            text="Restart Game",
            width=15,
            command=self.restart_game,
            state="disabled"
        )
        self.restart_btn.pack(pady=5)

    def check_guess(self):
        if self.attempts >= MAX_ATTEMPTS:
            return

        try:
            guess = int(self.entry.get())
        except ValueError:
            self.feedback_label.config(text="Enter a valid number!", fg="red")
            return

        if guess <= 0:
            self.feedback_label.config(text="Positive numbers only!", fg="red")
            return

        self.attempts += 1
        remaining = MAX_ATTEMPTS - self.attempts

        if guess == self.secret:
            messagebox.showinfo("Winner 🎯", "You guessed it right!")
            self.end_game()
        elif guess > self.secret:
            self.feedback_label.config(
                text=f"Too high! Attempts left: {remaining}", fg="orange"
            )
        else:
            self.feedback_label.config(
                text=f"Too low! Attempts left: {remaining}", fg="orange"
            )

        if self.attempts == MAX_ATTEMPTS and guess != self.secret:
            messagebox.showerror(
                "Game Over 😵",
                f"You Lost!\nThe number was {self.secret}"
            )
            self.end_game()

        self.entry.delete(0, tk.END)

    def end_game(self):
        self.submit_btn.config(state="disabled")
        self.restart_btn.config(state="normal")

    def restart_game(self):
        self.reset_game()
        self.feedback_label.config(text="Attempts left: 3", fg="blue")
        self.submit_btn.config(state="normal")
        self.restart_btn.config(state="disabled")
        self.entry.delete(0, tk.END)
        self.entry.focus()


if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGameGUI(root)
    root.mainloop()
