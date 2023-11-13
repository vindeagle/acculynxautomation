import requests
import json

# Ask user for the job ID
job_id = input("Enter the job ID: ")

# Define the API endpoint with the job ID
url = f"https://api.acculynx.com/api/v2/jobs/{job_id}/estimates"

# Define the headers
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer NWEwOTM1MDYtNGY4OC00YTU2LWFlNjUtMzM5NjZmZWUwNjc3MTQ5YWI1OTgtMmE1Ni00OWIwLTg2MzAtOGRjZWMxNjZmMjQ3"
}

# Send the GET request
response = requests.get(url, headers=headers)

# Print the response content
print(response.content)