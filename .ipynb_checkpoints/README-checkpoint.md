This is a project in which you can scrape all reviews from a specified review-web and analyse each one with a LSTM Neural Network.

If you just want to analyse a sentence with the NN, then you can!. This NN is previosly trained with NLTK movie_reviews dataset

How to use it?

---> Just write in console: python scrape_and_analyse.py (param_1) (param_2)

PARAMS:

- param_1: 0 if you want to use a pre-trained model or 1 if you want to train this model again
- param_2: 0 if you want to scrape a page(*) or 1 if you want to write a review to be analysed

(*) IMPORTANT!!!

Url must be this format: "https://www.metacritic.com/movie/movie-name/user-reviews" where "movie-name" changes according to the movie we have selected