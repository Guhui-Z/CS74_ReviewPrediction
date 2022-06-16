# Amazon Review Prediction Project
## Joseph Januszewicz, Josephine (Mien) Nguyen, Guhui Zhang

### Description
Code for data exploration, preprocessing, different pipeline approaches to predict whether an Amazon product is awesome or not, defined as whether its average review > 4.5 stars.

*Note: as this repo is made public, it does not contain the datasets for privacy concerns.*

### Feature Engineering

- ‘reviewText’ and ‘summary’:
    -  TF-IDF vectorizer; weighs ‘summary’ higher by concatenating it to the `reviewText` 5 times
- ‘view-buy’:
    - length of ‘buy_after_viewing’ in ‘related’
- ‘root-genre’:
    - binary encoding
- ‘reviewText’ and ‘summary’:
    - squared (VADER sentiment analysis scores + 1)
- ‘review-count’
    number of reviews per product!

### Model

XGBoostClassifier with eighted F1 10-fold cross validation: 0.76

### Instructions
`third_iteration_model.py` contains our final model's code. Please see the file for detailed documentation.

`second_iteration_model.py` contains the code of our second approach.

`first_iteration_model.py` contains the code of our first approach.

`data_exploration.py` contains the code of our data exploration (graphs, charts, etc.).

`data_preprocessing.py` contains preprocessing code, *most of which are unused in the final model*.

We tried our best to make sure that all the code that is used in our final model's pipeline is just in `third_iteration_model.py`, but we found some useful functions and preprocessing methods in earlier iterations, which we brought back in the final model. Thus, some functions in the final model are not in `third_iteration_model.py` to avoid code repetition. Please have every file in the same directory if you want to run the code.

Please also make sure `full_train.csv` (essentially `Train.csv` but with `target` column, which indicates product awesomeness) is in the directory, as the earlier iterations use it. We only adapted our final pipeline to work with the provided `Train.csv`.
