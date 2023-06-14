# import requests
# from bs4 import BeautifulSoup
# import csv

# def write_to_csv(data):
#     with open('data.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow([data['title'], data['description']])


# def get_html(url):
#     '''возвращает html код страницы'''
#     response = requests.get(url)
#     return response.text

# # def get_total_pages(html):
# #     soup = BeautifulSoup(html, 'lxml')
# #     last_page = soup.find('div', class_='nav-previous').find_all('a')
# #     list_page = last_page[1].text
# #     return int(last_page)

# url = 'http://kurak.kg/%d0%bc%d0%b5%d1%80%d0%be%d0%bf%d1%80%d0%b8%d1%8f%d1%82%d0%b8%d1%8f/'

# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     product_list = soup.find('div', class_='site-content').find_all('article', class_='post')
#     # print(product_list)
#     # global image
#     global title
#     global description
#     for product in product_list:
#         title = product.find('header', class_='entry-header').find('h1', class_='entry-title').text
        
#         description_list = product.find('div', class_='entry-content').find_all('p')
#         desc_ul = product.find('div', class_='entry-content').find_all('li')
#         desc = ' '.join([description_text.text for description_text in description_list])
#         descrip = ' '.join([description_text.text for description_text in desc_ul])
#         description = f'{desc} {descrip}'
#         # image =product.find('div', class_='entry-content').find('img').get('src')

#         dict_ = {'title':title, 'description':description}
#         # print(dict_)
#         write_to_csv(dict_)
        
# # get_data(get_html(url))


# def main():
#     ayim_url = 'http://kurak.kg/%d0%bc%d0%b5%d1%80%d0%be%d0%bf%d1%80%d0%b8%d1%8f%d1%82%d0%b8%d1%8f/'
#     pages = 'page/'
#     html = get_html(ayim_url)
#     # number = 10
#     # get_data(html)
#     # for i in range(2, number+1):
#     #     url_pages = f'{ayim_url}{pages}{str(i)}/'
#     #     html = get_html(url_pages)
#     #     get_data(html)

#     # base_url = 'http://kurak.kg/%d0%bc%d0%b5%d1%80%d0%be%d0%bf%d1%80%d0%b8%d1%8f%d1%82%d0%b8%d1%8f/'
#     # page = 1
#     # # get_data(get_html(base_url))
#     # while True:
#     #     url = f'{ayim_url}page/{page}/'
#     #     html = get_html(url)
#     #     # Парсить данные со страницы
#     #     get_data(html)
#     #     page += 1

# main()


import csv
import requests
from bs4 import BeautifulSoup

def write_to_csv(data):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['titles'], data['descriptions'], data['list_img']])


def get_html(url):
    '''возвращает html код страницы'''
    response = requests.get(url)
    return response.text

# def get_total_pages(html):
#     soup = BeautifulSoup(html, 'lxml')
#     last_page = soup.find('div', class_='nav-previous').find_all('a')
#     list_page = last_page[1].text
#     return int(last_page)

url = 'http://kurak.kg/%d0%bc%d0%b5%d1%80%d0%be%d0%bf%d1%80%d0%b8%d1%8f%d1%82%d0%b8%d1%8f/'

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    product_list = soup.find('div', class_='site-content').find_all('article', class_='post')
    # print(product_list)
    global list_img
    global titles
    global descriptions
    for product in product_list:
        titles = product.find('header', class_='entry-header').find('h1', class_='entry-title').text
        
        description_list = product.find('div', class_='entry-content').find_all('p')
        desc_ul = product.find('div', class_='entry-content').find_all('li')
        desc = ' '.join([description_text.text for description_text in description_list])
        descrip = ' '.join([description_text.text for description_text in desc_ul])
        descriptions = f'{desc} {descrip}'
        image_element = product.find('div', class_='entry-content').find('img')
        list_img = image_element.get('src') if image_element else None

        dict_ = {'titles':titles, 'descriptions':descriptions, 'list_img':list_img}
        # print(dict_)
        write_to_csv(dict_)
        
get_data(get_html(url))


def main():
    ayim_url = 'http://kurak.kg/%d0%bc%d0%b5%d1%80%d0%be%d0%bf%d1%80%d0%b8%d1%8f%d1%82%d0%b8%d1%8f/'
    html = get_html(ayim_url)
    # number = 10
    # get_data(html)
    # for i in range(2, number+1):
    #     url_pages = f'{ayim_url}{pages}{str(i)}/'
    #     html = get_html(url_pages)
    #     get_data(html)

    # base_url = 'http://kurak.kg/%d0%bc%d0%b5%d1%80%d0%be%d0%bf%d1%80%d0%b8%d1%8f%d1%82%d0%b8%d1%8f/'
    page = 1
    # get_data(get_html(base_url))
    while True:
        url = f'{ayim_url}page/{page}/'
        html = get_html(url)
        # Парсить данные со страницы
        get_data(html)
        page += 1

main()