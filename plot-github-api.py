import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
#make the API call and store the response
url = 'https://api.github.com/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ", r.status_code)
# Store API response in a variable
response_dict = r.json()
# process results
print("Total repositories:" response_dict['total_count'])
# Explore info about the repositories
repo_dicts = response_dict['items']
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
   # stars.append(repo_dict['stargazers_count'])

    plot_dict = {
        'value': repo_dict['stargazers_count'], 
        'labels': repo_dict['description'],
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)
# Make a visualization
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = "Highest-rated python projects on Github'
chart.x_labels = names
chart.add('', plot_dicts)

chart.render_to_file('python_repos.svg')

