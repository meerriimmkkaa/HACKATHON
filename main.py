from bs4 import BeautifulSoup
import requests
import csv


def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup

def get_data(soup):
    mashinas = soup.find_all('div',class_='list-item list-label')
    for mashina in mashinas:
        try:

            title = mashina.find('h2',class_='name').text.strip()
        except AttributeError:
            title = 'None'
        try:
            image = mashina.find('div', class_='thumb-item-carousel').find('img', class_='lazy-image').get('data-src')
        except AttributeError:
            image = 'None'
        try:
            price = mashina.find('strong').text.strip()
        except AttributeError:
            price = 'None'
        try:
            info = mashina.find('div', class_='block info-wrapper item-info-wrapper').text.strip()
        except AttributeError:
            info = 'None'
     
      
        write_csv({
            'title': title, 
            'image': image, 
            'price': price,
            'info': info
            })

def write_csv(data):
    with open('mashiny.csv', 'a') as file:
        names = ['title', 'price', 'image', 'info']
        write = csv.DictWriter(file, delimiter=',', fieldnames=names)
        write.writerow(data)

def main():
    for i in range(1, 20):
        BASE_URL = 'https://www.mashina.kg/search/all/'
        html = get_html(BASE_URL)
        soup = get_soup(html)
        print(get_data(soup))

    
main()



# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin git@github.com:meerriimmkkaa/HACKATHON.git
# git push -u origin main








# git init
# git status
# git add .
# git commit -m ' deh'
# git remote add origin @
# git push origin master

