import requests

estimate_id = input("Enter the estimate ID: ")

url = f"https://api.acculynx.com/api/v2/estimates/{estimate_id}"
params = {
    "pageSize": 1,
    "pageStartIndex": 0,
    "includes": "fef7a313-ada4-ade1-3b08-b77bccc048aa"
}
headers = {
    "accept": "application/json",
    "Authorization": "Bearer NWEwOTM1MDYtNGY4OC00YTU2LWFlNjUtMzM5NjZmZWUwNjc3MTQ5YWI1OTgtMmE1Ni00OWIwLTg2MzAtOGRjZWMxNjZmMjQ3"
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    try:
        data = response.json()
        profit_margin = data['profitMarginTotal']
        print(f"Profit Margin Total: {profit_margin}")
    except ValueError:
        print("Response content is not in valid JSON format.")
else:
    print(f"Error: {response.status_code}")
