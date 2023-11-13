import requests
import json

# Ask user for the job ID
job_id = input("Enter the job ID: ")

# Define the API endpoint with the job ID
url = f"https://api.acculynx.com/api/v2/jobs/{job_id}/comments"

# Define the headers
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer YjdmNmEyZjYtZWRhZC00MzhhLTg0NjctZDkwNjgxODhmMmRhYWEwOGYwY2ItNmY1NS00NDdkLWJjN2UtZmRlYzJlNTkzNjk4"
}

# Send the GET request
response = requests.get(url, headers=headers)

# Print the response content
print(response.content)

# Print the response status code
print(response.status_code)

# Extract the comments from the response
comments = json.loads(response.content)
comment_bodies = [comment["body"] for comment in comments]

# Print the comment bodies
for body in comment_bodies:
    print(body)