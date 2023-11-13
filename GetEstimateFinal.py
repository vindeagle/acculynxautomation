import requests

estimate_id = input("Enter the estimate ID: ")

url = f"https://api.acculynx.com/api/v2/estimates/{estimate_id}"


params = {
    "pageSize": 1,
    "pageStartIndex": 0,
}


headers = {
    "accept": "application/json",
    "Authorization": "Bearer NWEwOTM1MDYtNGY4OC00YTU2LWFlNjUtMzM5NjZmZWUwNjc3MTQ5YWI1OTgtMmE1Ni00OWIwLTg2MzAtOGRjZWMxNjZmMjQ3"
}



response = requests.get(url, params=params, headers=headers)

print(response.json())