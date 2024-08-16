import tkinter as tk
import random

# Initialize global variables for scores
player_score = 0
computer_score = 0
ties = 0

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Scissors" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
        return "win"
    else:
        return "lose"

# Function to update scores
def update_scores(result):
    global player_score, computer_score, ties
    if result == "win":
        player_score += 1
    elif result == "lose":
        computer_score += 1
    elif result == "tie":
        ties += 1
    update_score_display()

# Function to update the score display
def update_score_display():
    score_label.config(text=f"Player: {player_score}  |  Computer: {computer_score}  |  Ties: {ties}")

# Function to handle button clicks
def play(choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(choice, computer_choice)
    update_scores(result)
    show_result(result, computer_choice)

def show_result(result, computer_choice):
    result_window = tk.Toplevel(root)
    result_window.title("Result")
    result_window.configure(bg="#FFDDC1")  # Soft peach background

    # Center the result window on the screen
    result_window.update_idletasks()  # Update the window's geometry
    screen_width = result_window.winfo_screenwidth()
    screen_height = result_window.winfo_screenheight()
    window_width = 300
    window_height = 200
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    result_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Result message
    tk.Label(result_window, text=f"Computer chose {computer_choice}.\nYou {result}!",
             font=("Comic Sans MS", 16, "bold"), bg="#FFDDC1", fg="#BF5B2C").pack(pady=30)

    # Close button
    tk.Button(result_window, text="Close", command=result_window.destroy,
              font=("Comic Sans MS", 12, "bold"), bg="#BF5B2C", fg="white").pack(pady=10)

# Main function to set up the GUI
def main():
    global root, score_label
    root = tk.Tk()
    root.title("Rock Paper Scissors Game")
    root.geometry("450x350")
    root.configure(bg="#B2EBF2")  # Light cyan background

    # Title Label
    title_label = tk.Label(root, text="Rock Paper Scissors", font=("Comic Sans MS", 24, "bold"), bg="#B2EBF2", fg="#00796B")
    title_label.pack(pady=20)

    # Score Display
    score_label = tk.Label(root, text="Player: 0  |  Computer: 0  |  Ties: 0",
                           font=("Comic Sans MS", 16), bg="#B2EBF2", fg="#004D40")
    score_label.pack(pady=10)

    # Create Frame for Buttons
    button_frame = tk.Frame(root, bg="#B2EBF2")
    button_frame.pack(pady=20)

    # Define button styles
    button_style = {
        "font": ("Comic Sans MS", 14, "bold"),
        "width": 12,
        "height": 2,
        "bd": 0,
        "relief": "flat"
    }

    # Rock Button
    rock_button = tk.Button(button_frame, text="Rock", command=lambda: play("Rock"),
                           bg="#FF5722", fg="white", **button_style)
    rock_button.grid(row=0, column=0, padx=15, pady=10)

    # Paper Button
    paper_button = tk.Button(button_frame, text="Paper", command=lambda: play("Paper"),
                            bg="#4CAF50", fg="white", **button_style)
    paper_button.grid(row=0, column=1, padx=15, pady=10)

    # Scissors Button
    scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play("Scissors"),
                                bg="#03A9F4", fg="white", **button_style)
    scissors_button.grid(row=0, column=2, padx=15, pady=10)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()
