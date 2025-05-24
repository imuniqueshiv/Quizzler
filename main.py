# Importing necessary modules and classes
from question_model import Question  # Class to structure question data
from data import question_data  # List of questions fetched from the API
from quiz_brain import QuizBrain  # Class to handle quiz logic
from ui import QuizInterface  # Class to handle the user interface

# Creating a list to store question objects
question_bank = []
for question in question_data:  # Loop through each question in the fetched data
    question_text = question["question"]  # Extract the question text
    question_answer = question["correct_answer"]  # Extract the correct answer
    new_question = Question(question_text, question_answer)  # Create a Question object
    question_bank.append(new_question)  # Add the object to the question bank

# Initialize the quiz logic with the list of questions
quiz = QuizBrain(question_bank)

# Initialize the user interface and pass the quiz logic to it
quiz_ui = QuizInterface(quiz)

# Print a message when the quiz is completed
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")  # Display the final score