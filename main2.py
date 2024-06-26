import requests
from bs4 import BeautifulSoup as BS
from openpyxl import Workbook

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def get_data(html):
    soup = BS(html,'html.parser')
    container = soup.find('div', class_='container-fluid my-3x md:my-4x')
    posts = container.find_all('a',class_='p-2x flex flex-col gap-y-2x')


    data = []
    for post in posts:
        prices = post.find('div', class_='flex gap-x-0.5x')
        price = prices.find('span', class_='whitespace-nowrap text-title_4').text.strip().replace(" ", "")
        price_m2 = prices.find('p', class_='text-gray__dark_1 whitespace-nowrap text-caption').text.strip()
        description = post.find('p', class_='whitespace-nowrap truncate text-body_2').text.strip()
        location = post.find('p', class_='whitespace-nowrap text-gray__dark_2 truncate text-caption').text.strip()
        
        # print(f"Цена:{price},\n КВм:{price_m2},\n Локация:{location},\n Описание:{description}")
        data.append([price, price_m2, description, location])
    return data[:20]

def save_in_xls(data, filename='data.xlsx'):
    wb = Workbook()
    ws = wb.active

    # Записываем заголовки
    ws.append(['Price', 'Price per m2', 'Description', 'Location'])

    # Записываем данные
    for row in data:
        ws.append(row)

    # Сохраняем в файл data.xlsx
    wb.save(filename)
    print(f"Данные записались в {filename}")


def main():
    url = 'https://aqarmap.com.eg/en/for-sale/property-type/cairo/new-cairo/'
    html = get_html(url)
    if html:
        data = get_data(html)
        save_in_xls(data)
    else:
        print('Не сохранилось')


if __name__ == '__main__':
    main()