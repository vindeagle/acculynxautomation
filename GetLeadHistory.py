import requests

job_id = input("Enter the job ID: ")

api_key = "NWEwOTM1MDYtNGY4OC00YTU2LWFlNjUtMzM5NjZmZWUwNjc3MTQ5YWI1OTgtMmE1Ni00OWIwLTg2MzAtOGRjZWMxNjZmMjQ3"

url = f"https://api.acculynx.com/api/v2/jobs/{job_id}/history"

headers = {'accept': 'application/json', 'Authorization': f'Bearer {api_key}'}

response = requests.get(url, headers=headers)

print(response.json()) # or do whatever you want with the response
