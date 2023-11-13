import requests
import datetime
import smtplib

job_id = input("Enter the job ID: ")
api_key = "NWEwOTM1MDYtNGY4OC00YTU2LWFlNjUtMzM5NjZmZWUwNjc3MTQ5YWI1OTgtMmE1Ni00OWIwLTg2MzAtOGRjZWMxNjZmMjQ3"
url = f"https://api.acculynx.com/api/v2/jobs/{job_id}/history"
headers = {'accept': 'application/json', 'Authorization': f'Bearer {api_key}'}
response = requests.get(url, headers=headers)

history = response.json()['items']
last_action_date_str = history[0]['date']
last_action_date = datetime.datetime.fromisoformat(last_action_date_str[:-1]) # strip 'Z' and convert to datetime object
delta = datetime.datetime.utcnow() - last_action_date

if delta.days > 7:
    sender_email = "cbauer1127@gmail.com"
    sender_password = "FinnMinn20!"
    recipient_email = "bauejam13@gmail.com"
    message = f"Job {job_id} has not been updated in {delta.days} days."

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message)
    server.quit()

print(history) # or do whatever you want with the response
