import html
# Class to manage the quiz logic
class QuizBrain:

    def __init__(self, q_list):
        # Initialize the quiz with a list of questions
        self.question_number = 0  # Tracks the current question number
        self.score = 0  # Tracks the user's score
        self.question_list = q_list  # List of questions
        self.current_question = None  # Placeholder for the current question

    def still_has_questions(self):
        # Check if there are more questions left in the quiz
        return self.question_number < len(self.question_list)

    def next_question(self):
        # Fetch the next question and increment the question number
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # Decode HTML entities in the question text
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text} "

    def check_answer(self, user_answer):
        # Check if the user's answer matches the correct answer
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1  # Increment score if the answer is correct
            return True
        else:
            return False