# Class to represent a single question
class Question:

    def __init__(self, q_text, q_answer):
        # Initialize the question with its text and correct answer
        self.text = q_text  # The question text
        self.answer = q_answer  # The correct answer

        """
                This class is important because 
                it provides a structured way to store
                and manage each question and its corresponding answer.
                It acts as a blueprint for creating question objects,
                which are later used in the quiz logic to display questions 
                and validate answers.
                """