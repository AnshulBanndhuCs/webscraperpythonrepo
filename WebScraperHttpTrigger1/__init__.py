import logging
import time
import azure.functions as func
from playwright.sync_api import sync_playwright

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # Run the web scraping function
    logging.info('Running web scraper...')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.globotreks.com/destinations/india/fun-interesting-facts-india/")
        time.sleep(2)
        
        page.evaluate('window.scrollBy(0, 500)')
        time.sleep(2)
        page.evaluate('window.scrollBy(0, 500)')
        time.sleep(2)
        page.evaluate('window.scrollBy(0, 500)')
        time.sleep(2)
        page.evaluate('window.scrollBy(0, 500)')
        time.sleep(2)
        page.evaluate('window.scrollBy(0, 500)')
        time.sleep(2)
        page.evaluate('window.scrollBy(0, 500)')
        time.sleep(2)
        page.evaluate('window.scrollBy(0, 500)')
        time.sleep(2)
        
        xpath_list = [
            '//*[@id="inner-wrap"]/section/div/div[2]/header/h1',
            '//*[@id="post-27291"]/div/div[1]/h2[1]/strong',
            '//*[@id="post-27291"]/div/div[1]/h2[2]/strong',
            '//*[@id="post-27291"]/div/div[1]/h2[3]/strong',
            '//*[@id="post-27291"]/div/div[1]/h2[4]/strong',
            '//*[@id="post-27291"]/div/div[1]/h2[5]/strong'
        ]

        elements = []
        for xpath in xpath_list:
            element = page.query_selector(xpath)
            elements.append(element)
            time.sleep(2)
        
        result = ""
        for element in elements:
            text = element.inner_text()
            print(text)
            result += text + "\n"

        browser.close()
        
    return func.HttpResponse(f"Webpage text: \n{result}")

main(func.HttpRequest)