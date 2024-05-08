import requests
from bs4 import BeautifulSoup as BS

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def get_links(html):
    soup = BS(html,'html.parser')
    container = soup.find('div', class_='container-fluid my-3x md:my-4x')
    posts = container.find_all('a', class_='p-2x flex flex-col gap-y-2x')

    links = []
    for post in posts:
        # prices = post.find('div', class_='flex gap-x-0.5x')
        # price = prices.find('span', class_='whitespace-nowrap text-title_4').text.strip().replace(" ", "")
        # price_m2 = prices.find('p', class_='text-gray__dark_1 whitespace-nowrap text-caption').text.strip()
        # title = post.find('p', class_='whitespace-nowrap truncate text-body_2').text.strip()
        # location = post.find('p', class_='whitespace-nowrap text-gray__dark_2 truncate text-caption').text.strip()
        link = post.get('href')
        full_link = 'https://aqarmap.com.eg'+ link
        links.append(full_link)
    return links 

def get_posts(html):
    soup = BS(html,'html.parser')
    title = soup.find('div', class_='flex-1')
    price = title.find('span', class_='text-title_3').text.replace('EGP', '').strip()+ ' EGP'
    name = title.find('h3', class_="text-gray__dark_2 text-body_1").text.strip()
    param = soup.find('div',class_="flex flex-col gap-y-x")
    address = param.find('p',class_="text-gray__dark_2 whitespace-nowrap truncate text-body_2").text.strip()
    area = param.find('p',class_='text-gray__dark_2 whitespace-nowrap truncate text-body_1').text.strip()
    listing_details = soup.find('section', class_='flex flex-col gap-x w-full container-fluid')
    floor = listing_details.find('span',class_='flex-[70%] xl:flex-[70%] lg:flex-[65%] text-start text-gray__dark_2 text-body_1').text.strip()
    
    # to do
    # view = 
    # year_built =
    # listing_id =
    # Price_per_meter =  

    listing_description = soup.find('section', class_='gap-y-3x container-fluid grid grid-cols-12')
    descrip = listing_description.find('div',class_='col-span-9 flex flex-col gap-x').text.strip()

    print(descrip)

def main():
    URL = 'https://aqarmap.com.eg/en/for-sale/property-type/cairo/new-cairo/'
    html = get_html(URL)
    get_links(html)
    links = get_links(html)
    for link in links:
        detail_html = get_html(url=link)
        data = get_posts(html=detail_html)


    
if __name__ == '__main__':
    main()