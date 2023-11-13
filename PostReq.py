import requests

api_key = "YjdmNmEyZjYtZWRhZC00MzhhLTg0NjctZDkwNjgxODhmMmRhYWEwOGYwY2ItNmY1NS00NDdkLWJjN2UtZmRlYzJlNTkzNjk4" # replace with your actual API key
url = "https://api.acculynx.com/api/v2/jobs/search"
querystring = {"pageSize":"1","pageStartIndex":"0","includes":"0"}

search_term = input("Enter the search term: ")


payload = {
  "searchTerm": search_term,}



headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_key # add Authorization header with API key
}

response = requests.post(url, headers=headers, params=querystring, data=payload)

print(response.text)