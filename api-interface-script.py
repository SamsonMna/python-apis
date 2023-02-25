import requests
# Make an API call and store the response
url = 'https://api.website.com/your-query = #yaml, json'
r = requests.get(url)
print("Status code:" r.status code)
# Store API response in a variable
response_dict = r.json()
# process the results
print(response_dict.keys())

