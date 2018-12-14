# Costco Scrape
Scrape Costco website,get the products information includes products name,description,price and images.

This web scrape utilizes the BeautifulSoup and Selenium Webdriver libraries to fetch the following data from a Costco product page and load it into a CSV file:
- Product Name
- Product Description
- Price
- Embedded images

This script ONLY works for the **Costco** website. It will break for any other website. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for testing purposes. 

### Prerequisites:
- [Python 3.7.0](https://www.python.org/downloads/windows/), make sure in the installation directions to click "Default Path", and click the check button to install PIP as well

  Once Python 3.7 is installed:

  - [Webdriver](http://selenium-python.readthedocs.io/installation.html). Please install the **Chrome** version!
    ###### (Copy the path of the installed webdriver! You will need it in set up!)

  - Selenium: 
  
    `pip install selenium`

  - BeautifulSoup: 
  
    `pip install beautifulsoup4`

### Set Up:
1. In the **DriverPath.txt** file, paste the path of the webdriver you installed above

   `C:\Users\DAE\Downloads\Chromedriver`
   
2. If you installed a driver other than **Chrome**, open **Scrape.py** and do the following:
   
   On line 27, by default there is `driver = webdriver.Chrome(path_to_driver)`
   - For **Firefox**: `driver = webdriver.Firefox(path_to_driver)`
   - For **Safari**:  `driver = webdriver.Safari(path_to_driver)`

### Running:
For every iteration of scraping:
  1. RUN:get-searching-urls.py
     You will get the URLS.txt which include the url-lists of serching result.
     Note:urls = ['https://www.costco.ca/CatalogSearch?keyword=chocolate'] # You can change 'chocolate' to what you want.
  2. RUN scrape.py
     You will get OutputData.csv whick include all infomation of your searching results.
     And you will get a file named ImageUrls

  3. If you want to download all the images of your searching-result,
     RUN read_urls_download_images.py
     note:dir='C:\\Users\\T180P\\Desktop\\Tong\\WixWeb\\Pictures\\chocalate\\' # change to your directory.

  
### Authors:
- CHUDDY
- TONG