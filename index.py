# from flask import Flask, jsonify, request
# from flask_cors import CORS
# import requests
# from bs4 import BeautifulSoup

# app = Flask(__name__)
# CORS(app)
# app.debug = True  

# @app.route('/')
# def home():
#     return jsonify({'message': 'Welcome to the Racquet Finder API'})

# @app.route('/api/scrape/racquet_guys', methods=['GET'])
# def scrape_racquet_guys():
#     racquet_guys_url = "https://racquetguys.ca/collections/used-tennis-racquets"
#     racquet_guys_base_url = "https://cdn.shopify.com/s/files/1/0009/8235/1923/"
#     response = requests.get(racquet_guys_url)
#     racquet_guys_soup = BeautifulSoup(response.text, 'html.parser')

#     racquet_guys_items = []

#     for racquet in racquet_guys_soup.find_all('div', class_='boost-pfs-filter-product-item-inner'):
#         name = racquet.find('a', class_='boost-pfs-filter-product-item-title').text
#         price = racquet.find('span', class_="boost-pfs-filter-product-item-sale-price").text
        
#         img_tag = racquet.find('img', class_='boost-pfs-filter-product-item-main-image')
#         if img_tag and 'data-src' in img_tag.attrs:
#             image_url = img_tag['data-src']
#             if image_url.startswith('//'):
#                 img = 'https:' + image_url
#             else:
#                 index = image_url.find('/files/')
#                 extracted_part = image_url[index + 1:]
#                 img = racquet_guys_base_url + extracted_part

#         seller = "Racquet Guys"

#         racquet_guys_items.append({
#             'name': name,
#             'price': price,
#             'image_url': img,
#             'seller': seller
#         })

   
#     return jsonify(racquet_guys_items)

# @app.route('/api/scrape/tads', methods=['GET'])
# def scrape_tads():
#     tads_url = "https://tadssportinggoods.ca/collections/clearance-tennis-rackets"
#     tads_response = requests.get(tads_url)
#     tads_soup = BeautifulSoup(tads_response.text, 'html.parser')
#     tads_base_url = 'https:'

#     tads_items = []

#     for racquet in tads_soup.find_all('div', class_="grid__item small--one-half medium-up--one-fifth"):
#         name_tag = racquet.find('div', class_="product-card__name")
#         price_tag = racquet.find('div', class_="product-card__price")
#         img_tag = racquet.find('img', class_="product-card__image")

    
#         if price_tag:
#             name = name_tag.text.replace("TENNIS RACKET", "")
            

#             sale_price_text = racquet.find(text="Sale price")
#             if sale_price_text:
#                 price = sale_price_text.find_next(string=True)
#             else:
#                 price = price_tag.text 
        
       
#             dollarIndex = price.find("$")
#             first_part = price[dollarIndex: ]
#             clean_price = '$'

#             for c in first_part:
#                 if (c.isdigit() or c == '.'):
#                     clean_price += c

       
#             img_url = img_tag['src']
#             seller = 'Tads Sporting Goods'
        
#             tads_items.append({
#                 'name': name,
#                 'price': clean_price,
#                 'image_url': tads_base_url + img_url,
#                 'seller': seller
#             })




#     return jsonify(tads_items)


# @app.route('/api/scrape/merchant', methods=['GET'])
# def scrape_merchant():
    
    
#     maxPrice = request.args.get('maxPrice', 1000)
#     maxPrice = float(maxPrice)
#     print(maxPrice)

#     merchant_url = "https://www.merchantoftennis.com/collections/clearance-racquets/adult-racquets"
#     merchant_base_url1 = "https:"
#     merchant_base_url2 = "https://www.merchantoftennis.com/"
#     response = requests.get(merchant_url)

#     merchant_soup = BeautifulSoup(response.text, 'html.parser')
#         #print(merchant_soup)

#     merchant_items = []

#     for racquet in merchant_soup.find_all('div', class_='item-list'):
    
#         racquet_info = racquet.find('div', class_='il-info')
#         name = racquet_info.find('a')
#         name = name.text.strip()
#         #print(name)
#         price = racquet_info.find('span', class_ ='current-value')
#         price = price.text.strip()
#         price = price.replace("$", "")
#         #print(price)

#         racquet_preview = racquet.find('div', class_ = "il-preview")
#         img = racquet_preview.find('img')
#         img = img['src']
#         img = merchant_base_url1 + img

#         #print(img)

#         link = racquet_preview.find('a')
#         link = link['href']
#         link = merchant_base_url2 + link
#         #print(link)

#         seller = "Merchant of Tennis"

#         merchant_items.append({
#             'name': name,
#             'price': "$" + price,
#             'image_url': img,
#             'seller': seller,
#             'link': link
#             })
    

#     # Filter items by price
#     filtered_items = [item for item in merchant_items if float(item['price'].replace('$', '')) <= maxPrice]
#     price_sorted = sorted(filtered_items, key=lambda x: float(x['price'].replace('$', ''))) 
#     print(filtered_items[0])
#     print(price_sorted[0])
    
#     return jsonify(price_sorted)

# @app.route('/test')
# def test():
#     return 'This is a test response'



# if __name__ == '__main__':
    
#     app.run(host='0.0.0.0')

from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)
app.debug = True  

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Racquet Finder API'})

@app.route('/api/scrape/racquet_guys', methods=['GET'])
def scrape_racquet_guys():
    racquet_guys_url = "https://racquetguys.ca/collections/used-tennis-racquets"
    racquet_guys_base_url = "https://cdn.shopify.com/s/files/1/0009/8235/1923/"
    response = requests.get(racquet_guys_url)
    racquet_guys_soup = BeautifulSoup(response.text, 'html.parser')

    racquet_guys_items = []

    for racquet in racquet_guys_soup.find_all('div', class_='boost-pfs-filter-product-item-inner'):
        name = racquet.find('a', class_='boost-pfs-filter-product-item-title').text
        price = racquet.find('span', class_="boost-pfs-filter-product-item-sale-price").text
        
        img_tag = racquet.find('img', class_='boost-pfs-filter-product-item-main-image')
        if img_tag and 'data-src' in img_tag.attrs:
            image_url = img_tag['data-src']
            if image_url.startswith('//'):
                img = 'https:' + image_url
            else:
                index = image_url.find('/files/')
                extracted_part = image_url[index + 1:]
                img = racquet_guys_base_url + extracted_part

        seller = "Racquet Guys"

        racquet_guys_items.append({
            'name': name,
            'price': price,
            'image_url': img,
            'seller': seller
        })

   
    return jsonify(racquet_guys_items)

@app.route('/api/scrape/tads', methods=['GET'])
def scrape_tads():
    tads_url = "https://tadssportinggoods.ca/collections/clearance-tennis-rackets"
    tads_response = requests.get(tads_url)
    tads_soup = BeautifulSoup(tads_response.text, 'html.parser')
    tads_base_url = 'https:'

    tads_items = []

    for racquet in tads_soup.find_all('div', class_="grid__item small--one-half medium-up--one-fifth"):
        name_tag = racquet.find('div', class_="product-card__name")
        price_tag = racquet.find('div', class_="product-card__price")
        img_tag = racquet.find('img', class_="product-card__image")

    
        if price_tag:
            name = name_tag.text.replace("TENNIS RACKET", "")
            

            sale_price_text = racquet.find(text="Sale price")
            if sale_price_text:
                price = sale_price_text.find_next(string=True)
            else:
                price = price_tag.text 
        
       
            dollarIndex = price.find("$")
            first_part = price[dollarIndex: ]
            clean_price = '$'

            for c in first_part:
                if (c.isdigit() or c == '.'):
                    clean_price += c

       
            img_url = img_tag['src']
            seller = 'Tads Sporting Goods'
        
            tads_items.append({
                'name': name,
                'price': clean_price,
                'image_url': tads_base_url + img_url,
                'seller': seller
            })




    return jsonify(tads_items)


@app.route('/api/scrape/merchant', methods=['GET'])
def scrape_merchant():
    
    
    maxPrice = request.args.get('maxPrice', 1000)
    maxPrice = float(maxPrice)
    print(maxPrice)

    merchant_url = "https://www.merchantoftennis.com/collections/clearance-racquets/adult-racquets"
    merchant_base_url1 = "https:"
    merchant_base_url2 = "https://www.merchantoftennis.com/"
    response = requests.get(merchant_url)

    merchant_soup = BeautifulSoup(response.text, 'html.parser')
        #print(merchant_soup)

    merchant_items = []

    for racquet in merchant_soup.find_all('div', class_='item-list'):
    
        racquet_info = racquet.find('div', class_='il-info')
        name = racquet_info.find('a')
        name = name.text.strip()
        #print(name)
        price = racquet_info.find('span', class_ ='current-value')
        price = price.text.strip()
        price = price.replace("$", "")
        #print(price)

        racquet_preview = racquet.find('div', class_ = "il-preview")
        img = racquet_preview.find('img')
        img = img['src']
        img = merchant_base_url1 + img

        #print(img)

        link = racquet_preview.find('a')
        link = link['href']
        link = merchant_base_url2 + link
        #print(link)

        seller = "Merchant of Tennis"

        merchant_items.append({
            'name': name,
            'price': "$" + price,
            'image_url': img,
            'seller': seller,
            'link': link
            })
    

    # Filter items by price
    filtered_items = [item for item in merchant_items if float(item['price'].replace('$', '')) <= maxPrice]
    price_sorted = sorted(filtered_items, key=lambda x: float(x['price'].replace('$', ''))) 
    print(filtered_items[0])
    print(price_sorted[0])
    
    return jsonify(price_sorted)

@app.route('/test')
def test():
    return 'This is a test response'


if __name__ == '__main__':
    
    app.run(host='0.0.0.0')