
import requests
# Sending a GET request to the Open Trivia Database API with specified parameters
parameter = {
    "amount": 10,  # Number of questions to fetch
    "type": "boolean",  # Question type (True/False)
    "category": 18,  # Category ID for Science: Computers
}

# Making the API request
response = requests.get(url="https://opentdb.com/api.php", params=parameter)
response.raise_for_status()  # Raise an exception for HTTP errors

# Parsing the JSON response
data = response.json()
question_data = data["results"]  # Extracting the list of questions