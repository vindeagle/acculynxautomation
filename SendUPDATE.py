import requests
import smtplib
from email.mime.text import MIMEText

job_id = input("Enter the job ID: ")
api_key = "NWEwOTM1MDYtNGY4OC00YTU2LWFlNjUtMzM5NjZmZWUwNjc3MTQ5YWI1OTgtMmE1Ni00OWIwLTg2MzAtOGRjZWMxNjZmMjQ3"
url = f"https://api.acculynx.com/api/v2/jobs/{job_id}/history"
headers = {'accept': 'application/json', 'Authorization': f'Bearer {api_key}'}
response = requests.get(url, headers=headers)

# Extract the latest action and the date it occurred
latest_action = response.json()['items'][0]['action']
latest_date = response.json()['items'][0]['date']

# Define the email message
subject = "Job Update"
body = f"The latest action on the job is: {latest_action}\nIt was last updated on: {latest_date}"
sender_email = "cbauer1127@gmail.com"
recipient_email = "bauejam13@gmail.com"
message = MIMEText(body)
message['Subject'] = subject
message['From'] = sender_email
message['To'] = recipient_email

# Send the email
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "cbauer1127"
smtp_password = "FinnMinn20!"
smtp_conn = smtplib.SMTP(smtp_server, smtp_port)
smtp_conn.starttls()
smtp_conn.login(smtp_username, smtp_password)
smtp_conn.sendmail(sender_email, recipient_email, message.as_string())
smtp_conn.quit()

print("Email sent!")