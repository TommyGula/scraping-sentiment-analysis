import keras
import argparse

from sentiment_analysis_model import predict_one
from sentiment_analysis_model import scrape_and_predict
from sentiment_analysis_model import get_model
from movies_scraping import scrape

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Facebook Page Scraper")
    required_parser = parser.add_argument_group("required arguments")
    required_parser.add_argument('-model', '-m', help="Write 0 if you want to use a pre-trained model or 1 if you want to train this model again", required=True)
    required_parser.add_argument('-scrape', '-s', help="Write 0 if you want to scrape a page(*) or 1 if you want to write a review to be analysed", required=True)
    args = parser.parse_args()

    model = 0
    if args.model == '0':
        model = keras.models.load_model('trained_model.h5')
    elif args.model == '1':
        model = get_model()
    else:
        print("You have to choose between 0 and 1")

    
    review = 0

    if args.scrape == '1':
        review = input("Write your sentence or review ")
        predicted = predict_one(review, model)
        print("Predicted value for your review is: ", predicted[0][0])
    elif args.scrape == '0':
        url = input("Paste page url you want to scrape ")
        reviews = scrape(url)
        predicted = scrape_and_predict(reviews, model)
        print("Predicted values are:\n", predicted)
    else:
        print("You have to choose between 0 and 1")
