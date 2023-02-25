import requests
#make the API call and store the response
url = 'https://api.github.com/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status code)
# Store API response in a variable
response_dict = r.json()
# process results
print("Total repositories:" response_dict['total_count'])
# Explore info about the repositories
repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))

#Examine the first repository
repo_dict = repo_dicts[0]
print("\nkeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
    

