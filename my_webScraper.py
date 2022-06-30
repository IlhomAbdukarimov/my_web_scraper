import requests
from bs4 import BeautifulSoup

def request_github_trending(url):
    return requests.get(url)

def extract(page):
    soap= BeautifulSoup(page.text, "html.parser")
    return soap.find_all("article")

def transform(html_repos):
    result=[]
    for row in html_repos:
        repository_name = ''.join(row.select_one("h1.h3.lh-condensed").text.split())
        num_stars = ''.join(row.select_one("span.d-inline-block.float-sm-right").text.split())
        developer_name = row.select_one("img.avatar.mb-1.avatar-user")['alt']
        result.append({'deverloper': developer_name, 'repository_name': repository_name, 'nbr_stars': num_stars})
    return result

def format(repositories_data):
    result = ["Developer, Repository Name, Number of Stars"]

    for repos in repositories_data:
        row = [repos['deverloper'], repos['repository_name'], repos['nbr_stars']]
        result.append(','.join(row))
    return "\n".join(result)

def _main():
    url = "https://github.com/trending"
    page = request_github_trending(url)
    html_repos = extract(page)
    repositeries_data = transform(html_repos)
    print(format(repositeries_data))
    

_main()
