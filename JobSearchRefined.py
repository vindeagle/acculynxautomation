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

# Parse the response content
json_data = json.loads(response.content)

# Extract the required parameters from the response
results = json_data.get('results', [])

for result in results:
    job_name = result.get('jobName', '')
    location_address = result.get('locationAddress', '')
    city = result.get('city', '')
    print(f"Job Name: {job_name}, Location Address: {location_address}, City: {city}")
