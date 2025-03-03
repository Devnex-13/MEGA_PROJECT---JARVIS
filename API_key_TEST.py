import requests

# Your API key
key = " "

# URL to test (for example, fetching top headlines)
url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={key}'

# Make a request to the API
response = requests.get(url)

# Check the response status
if response.status_code == 200:
    print("API key is working!")
    print(response.json())  # Print the response data
else:
    print(f"API request failed with status code: {response.status_code}")
    print(response.json())  # This will provide the error message from the API

# if output Is 200 Then Its Working.
# If Output is 401 means key is Not Working.