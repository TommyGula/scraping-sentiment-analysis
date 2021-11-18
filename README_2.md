# SCRAPING SENTIMENT ANALYSIS
*This is a project in which you can scrape all reviews from a specified review-web and analyse each one with a LSTM Neural Network.*

If you just want to analyse a sentence with the NN, then you can!. This NN is previosly trained with NLTK movie_reviews dataset

How to use it?

---> Just write in console: python scrape_and_analyse.py -model -scrape

PARAMS:

-model: 0 if you want to use a pre-trained model or 1 if you want to train this model again
-scrape: 0 if you want to scrape a page(*) or 1 if you want to write a review to be analysed

**(*) IMPORTANT!!!**

Url must be this format: "https://www.metacritic.com/movie/movie-name/user-reviews" where "movie-name" changes according to the movie we have selected

*RESPONSES*

1) If you typed -s 0, you'll get the reviews dataframe with all it's predictions and a confusion matrix of the model's performance

2) If you typed -s 1, you'll get the predicted value for the input sentence

