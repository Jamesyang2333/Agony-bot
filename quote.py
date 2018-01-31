# import the module that is necessary for the scraper
import requests
from bs4 import BeautifulSoup


class Quote(object):
    # Define the function that can read and store the whole HTML content of a certain web page
    def getHTML(self, url):
        r = requests.get(url)
        return r.content
        
    # define the function that can specificly figure out where the target quote is.
    # As we have noticed, the quote that follows this path is different every day because the website programmers update a new quote to this path everyday.
    def parseHTML(self, html):
        soup = BeautifulSoup(html,'html.parser')
        body = soup.body
        layer_one = body.find('strong',attrs={'style':'color: #0b5394;'})
        layer_two = body.find('div',attrs={'style':'text-align: center; margin-top: -18px; margin-bottom: 18px;'}) #The path of the target quote and its writer
        writer=layer_two.get_text()
        quote=layer_one.get_text()
        return writer, quote


# Instantiate a Quote object and specify the url of the target website        
quote = Quote()
URL = 'http://www.dailyenglishquote.com'



html = quote.getHTML(URL)
writer, quote = quote.parseHTML(html)


# this scraper will push the quote to users as a gift/bonus after they share their thoughts to the bot.
