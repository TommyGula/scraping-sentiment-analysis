#To get the url, and scrap the html page  
import requests
from bs4 import BeautifulSoup
#To save the reviews in a dataframe 
import pandas as pd

def scrape(url):
    
    # Config
    
    user_agent = {'User-agent': 'Chrome/95.0'}
    response = requests.get(url, headers = user_agent)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Define dict
    
    review_dict = {'name':[], 'date':[], 'rating':[], 'review':[]}
    
    # look for review_content tags since every user review has this tag
 
    for review in soup.find_all('div', class_='summary'): 
        #within review_content tag, look for the presence of longer reviews
        if review.find('span', class_='blurb blurb_expanded'): 
            review_dict['review'].append(review.find('span', class_='blurb blurb_expanded').text)

        else: 
            review_dict['review'].append(review.find('div',class_='review_body').find('span').text)
            
    return review_dict
