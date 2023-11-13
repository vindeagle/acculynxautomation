import requests

# Ask user for the job ID
job_id = input("Enter the job ID: ")

# Define the API endpoint
url = f"https://api.acculynx.com/api/v2/jobs/{job_id}/estimates"

# Define the headers
headers = {
    "accept": "application/json",
    "Authorization": "Bearer YOUR_API_KEY"
}

# Define the query parameters
params = {
    "pageStartIndex": "0"
}

# Send the GET request
response = requests.get(url, headers=headers, params=params)

# Save the response content as a PDF file on the desktop
file_path = r"C:/Users/cbaue/Desktop/GptTestFiles/estimate.pdf" # Replace with your desired file path
with open(file_path, 'wb') as f:
    f.write(response.content)