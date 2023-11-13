import requests
from bs4 import BeautifulSoup

# Make a GET request to the webpage
response = requests.get('https://www.quora.com/How-can-I-extract-the-main-text-from-any-given-webpage')

# Parse the HTML content of the webpage using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the section of the webpage using a CSS selector
question_section = soup.select_one('div.ul.q-box:nth-child(12)')

# Extract the text from the section, if it exists
if question_section is not None:
    question_text = question_section.get_text()
    print(question_text)
else:
    print("Could not find question section on the page.")