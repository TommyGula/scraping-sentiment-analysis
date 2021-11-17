# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define functions
def scrape_name(soup):
    names = []
    for review in soup.find_all('div', class_='title pad_btm_half'):
        names.append(review.find('span', class_='author').text)
    return names

def scrape_date(soup):
    dates = []
    for review in soup.find_all('div', class_='title pad_btm_half'):
        dates.append(review.find('span', class_='date').text)
    return dates

def scrape_rating(soup):
    ratings = []
    for review in soup.find_all('div', class_='left fl'):
        ratings.append(review.find('div').text)
    return ratings

def scrape_review(soup):
    reviews = []
    for review in soup.find_all('div', class_='summary'): 
    #within review_content tag, look for the presence of longer reviews
        if review.find('span', class_='blurb blurb_expanded'): 
            reviews.append(review.find('span', class_='blurb blurb_expanded').text)

        else: 
            reviews.append(review.find('div',class_='review_body').find('span').text)
    return reviews

# Final function and create Dataframe

def scrape(url):    
    # Config
    user_agent = {'User-agent': 'Chrome/95.0'}
    response = requests.get(url, headers = user_agent)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Define dict
    review_dict = {'name':[], 'date':[], 'rating':[], 'review':[]}
    
    # look for review_content tags since every user review has this tag
    review_dict['name'] = scrape_name(soup)
    review_dict['review'] = scrape_review(soup)
    review_dict['date'] = scrape_date(soup)
    review_dict['rating'] = scrape_rating(soup)
    
    response_df = pd.DataFrame(review_dict)
            
    return response_df
