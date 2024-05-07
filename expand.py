import requests
from bs4 import BeautifulSoup as BS

file = open('expannd_html.html', encoding='utf-8')

html = file.read()

soup = BS(html, 'html.parser')

main_div = soup.find('div', class_='container')
navigation = main_div.find('div', class_='navigation')
# ul = navigation.find('ul',class_='info')
# li_list = ul.find_all('li')
# for i in li_list:
#     print(i.text)


# content = main_div.find('div', class_='content')
# posts = content.find_all('div', class_='post')

# for post in posts:
#     title = post.find('h2', class_='title').text
#     print(title)

foot =  main_div.find('div', class_='footer')
footer_boxes = foot.find_all('div', class_='footer-box')

for i in footer_boxes:
    title = i.find('p', class_= 'footer-title').text
    print(title)