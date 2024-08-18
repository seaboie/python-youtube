<a id="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="">
    <img src="https://raw.githubusercontent.com/seaboie/images/main/images/logoTransparent.png" alt="Logo" width="120" height="120">
  </a>

  <h3 align="center">Web Scraping</h3>

  <p align="center">
    Ultimate Guide To Web Scraping - Node.js & Python (Puppeteer & Beautiful Soup)
    <br />
    <a href="https://www.youtube.com/watch?v=XMu46BRPLqA"><strong>On Youtube 33:40»</strong></a>
    <br />
    
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#trick">Trick</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>




<!-- GETTING STARTED -->
## Getting Started


### Prerequisites
Create virtual environment  
```bash
python3 -m venv env
```  
```bash
source env/bin/activate
```  
we will get `(env)`
```bash
krit@Macintosh python-youtube % python3 -m venv env
krit@Macintosh python-youtube % source env/bin/activate
(env) krit@Macintosh python-youtube %
```  

> To exit a virtual environment in the terminal  
```bash
deactivate
```  

### Installation
Install 2 package `requests` and `beautifulsoup4`  
```bash
pip install requests beautifulsoup4 
```  

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Trick  

> **Check** : if no directory create it  `os.makedirs(data_directory, exist_ok=True)`  
> **Write** : data to file json format

```python
import os   # --- import os
import json # --- import json


# declare variable
data_directory = './data'


# --- Create the directory if it doesn't exist
os.makedirs(data_directory, exist_ok=True)

# Now save the JSON file
with open(os.path.join(data_directory, 'books.json'), 'w') as f:
    json.dump(all_books, f, indent=2)
``` 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

> `scrape.py`  

```python
def fetch_books(page_number):
    url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"
    linkUrl = f"https://books.toscrape.com/catalogue/"
    baseUrl = f"https://books.toscrape.com/"
    books = []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # books elements
        book_elements = soup.find_all('article', class_='product_pod')

        # loops
        for book in book_elements:
            title = book.find('h3').find('a')['title']
            link_element = book.find('h3').find('a')['href']
            link = linkUrl + link_element
            price = book.find('p', class_='price_color').text.replace('Â', '')

            # image
            imageUrl = book.find('div', class_='image_container').find('a').find('img')['src']
            image = baseUrl + imageUrl
            # instock
            availability_text = book.find('p', class_='instock availability').text
            instock = 'In stock' if 'In stock' in availability_text else 'Out of stock'
            # rating
            rating_element = book.find('p', class_='star-rating')
            get_class_index_rating = rating_element['class'][1]


            books.append({
                "title": title,
                "price": price,
                "stock": instock,
                "rating": get_class_index_rating,
                "link": link,
                "image_url": image,
            });
            
        return books

    except Exception as e:
        print("🔥 🔥 🔥 🔥 🔥 Oops !!! : ", e)
```  


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- ACKNOWLEDGMENTS -->
## Acknowledgments  

* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[logo-image]:https://raw.githubusercontent.com/seaboie/images/main/images/logoTransparent.png

