import requests
import json

# Ask user for the search term
search_term = input("Enter the search term: ")

# Define the API endpoint
url = "https://api.acculynx.com/api/v2/jobs/search"

# Define the headers
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer NWEwOTM1MDYtNGY4OC00YTU2LWFlNjUtMzM5NjZmZWUwNjc3MTQ5YWI1OTgtMmE1Ni00OWIwLTg2MzAtOGRjZWMxNjZmMjQ3"
}

# Define the request body
request_body = {
    "searchTerm": search_term,
}

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(request_body))

# Print the response contentmr gpt
print(response.content)