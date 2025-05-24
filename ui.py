from tkinter import *
from quiz_brain import QuizBrain

# Define a theme color for the app
THEME_COLOR = "#375362"

# Class to handle the user interface
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # Initialize with the quiz logic
        self.quiz = quiz_brain
        self.score = 0

        # Create the main window
        self.window = Tk()
        self.window.title("Quizzler")  # Set the title of the window
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)  # Add padding and background color

        # Add a label to display the score
        self.label = Label(text="Score: 0", font=("Arial", 14, "italic"), bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)  # Position the label

        # Add a canvas to display the question
        self.canvas = Canvas(width=300, height=250, bg="white")  # Create a white canvas
        self.canvas.config(highlightthickness=0)  # Remove border
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Question text goes here",
            font=("Arial", 20, "italic"), fill=THEME_COLOR
        )  # Add placeholder text
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)  # Position the canvas

        # Add buttons for "True" and "False" answers
        self.image = PhotoImage(file="images/true.png")  # Load the "True" button image
        self.right_button = Button(self.window, image=self.image, command=self.right_click, highlightthickness=0)
        self.right_button.grid(row=2, column=0)  # Position the "True" button

        self.image_ = PhotoImage(file="images/false.png")  # Load the "False" button image
        self.wrong_button = Button(self.window, image=self.image_, command=self.wrong_click, highlightthickness=0)
        self.wrong_button.grid(row=2, column=1)  # Position the "False" button

        # Load the first question
        self.get_next_question()

        # Bind the Escape key to close the app
        self.window.bind("<Escape>", lambda event: self.window.quit())

        # Start the main event loop
        self.window.mainloop()

    # Function to load the next question
    def get_next_question(self):
        self.canvas.config(bg="white")  # Reset the canvas background color
        if self.quiz.still_has_questions():  # Check if there are more questions
            self.label.config(text=f"Score: {self.quiz.score}")  # Update the score
            q_text = self.quiz.next_question()  # Get the next question
            self.canvas.itemconfig(self.question_text, text=q_text)  # Display the question
        else:
            # If no more questions, display a completion message
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz")
            self.canvas.config(bg="white")  # Reset the canvas background
            self.right_button.config(state="disabled")  # Disable the "True" button
            self.wrong_button.config(state="disabled")  # Disable the "False" button

    # Function to handle the "True" button click
    def right_click(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))  # Check the answer and give feedback

    # Function to handle the "False" button click
    def wrong_click(self):
        is_right = self.quiz.check_answer(user_answer="False")  # Check the answer
        self.give_feedback(is_right)  # Give feedback

    # Function to give feedback based on the answer
    def give_feedback(self, is_right):
        if is_right:  # If the answer is correct
            self.canvas.config(bg="green")  # Change the canvas background to green
        else:  # If the answer is incorrect
            self.canvas.config(bg="red")  # Change the canvas background to red
        self.window.after(1000, self.get_next_question)  # Wait 1 second and load the next question