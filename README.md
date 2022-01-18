
# SCRAPING SENTIMENT ANALYSIS

*This is a project in which you can scrape all reviews from a specified review-web and analyse each one with a LSTM Neural Network.*

If you just want to analyse a sentence with the NN, then you can!. This NN is previosly trained with NLTK movie_reviews dataset

How to use it?

---> Just write in console: python scrape_and_analyse.py -model -scrape

PARAMS:

-model: 0 if you want to use a pre-trained model or 1 if you want to train this model again

-scrape: 0 if you want to scrape a page(*) or 1 if you want to write a review to be analysed

**(*) IMPORTANT!!!**

Url must be this format: "https://www.metacritic.com/movie/movie-name/user-reviews" where "movie-name" changes according to the movie you have selected

*RESPONSES*

1) If you typed -s 0, you'll get the reviews dataframe with all it's predictions and a confusion matrix of the model's performance

2) If you typed -s 1, you'll get the predicted value for the input sentence

*Example*

1) scrape_and_analyse.py -m 0 -s 0 ---> Then you must pass an url for the movie you chose, and it will scrape the full page and analyse its reviews
2) scrape_and_analyse.py -m 0 -s 1 ---> You have chosen "-s 1" so no url is needed. All you must do is writting a review by yourself and it will be analysed

