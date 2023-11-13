import requests

api_key = "YjdmNmEyZjYtZWRhZC00MzhhLTg0NjctZDkwNjgxODhmMmRhYWEwOGYwY2ItNmY1NS00NDdkLWJjN2UtZmRlYzJlNTkzNjk4"
url = "https://virtserver.swaggerhub.com/AccuLynx/PublicAPI/2.2222.0/jobs/search"


headers = {"Authorization": f"Bearer {api_key}"}

search_params = {
    "searchTerm": "Na Na na",
    }


response = requests.get(url, headers=headers, params=search_params)

if response.status_code == 200:
    data = response.json()
    if "jobs" in data:
        for job in data["jobs"]:
            # Do something with the job data here
            print(job) # print the job information
    else:
        print("No jobs found in response data")
else:
    print(f"Error: {response.status_code} - {response.reason}")