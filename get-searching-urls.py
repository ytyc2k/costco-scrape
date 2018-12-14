from bs4 import BeautifulSoup, NavigableString #extract the html from the request
from selenium import webdriver #deal with the dynamic javascript
from multiprocessing import Process

#URLs of the specific products
URLS = []

#Load the path of the driver for use
def load_driver_path():
    path_file = open('DriverPath.txt', 'r')
    path = path_file.read().strip()
    path_file.close()
    return path

def load_urls_from_search_file():
    #urls_file = open('URLS.txt', 'r')
    #urls = urls_file.readlines()
    urls = ['https://www.costco.ca/CatalogSearch?keyword=chocolate']
    for url in urls:
        URLS.append(url.strip())
    #urls_file.close()

#Loads all the urls from the URLS.txt file and appends them to the array of urls
def load_urls_from_text_file():
    urls_file = open('URLS.txt', 'r')
    urls = urls_file.readlines()
    for url in urls:
        URLS.append(url.strip())
    urls_file.close()

#Establish the webdriver
def link_driver(path_to_driver):
    #Establish the driver
    driver = webdriver.Chrome(path_to_driver)
    return driver

#  1. Loads the html data
#  2. Turns it into soup
def load_data(webdriver):
    for url in URLS:
        #Get the contents of the URL
        webdriver.get(url)

        #returns the inner HTML as a string
        innerHTML = webdriver.page_source

        #turns the html into an object to use with BeautifulSoup library
        soup = BeautifulSoup(innerHTML, "html.parser")

        extract_and_load_all_data(soup)

#closes the driver
def quit_driver(webdriver):
    webdriver.close()
    webdriver.quit()

# Load data to file URLS.txt
def extract_and_load_all_data(soup):
    tag = soup.findAll('p', class_='description')
    tag = [i.a['href'] for i in tag]
    with open('URLS.txt', 'w') as f:
        for item in tag:
            f.write("%s\n" % item)



    #output_data.close()

#  1. Links the driver
#  2. Loads the html data
#  3. Turns it into soup
#  4. extracts correct elements and loads it to csv file
def run():
    load_urls_from_search_file()
    path = load_driver_path()
    driver = link_driver(path)
    load_data(driver)
    quit_driver(driver)

def main():
    #create multiple threads for selenium web scraping - ASYNC
    processes = []
    p = Process(target=run, args=())
    processes.append(p)
    p.start()

    for p in processes:
        p.join()

if __name__ == "__main__":
    main()
