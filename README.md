# Predicting Survival on the Titanic

## History
Perhaps one of the most infamous shipwrecks in history, the Titanic sank after colliding with an iceberg, killing 1502 out of 2224 people on board. Interestingly, by analysing the probability of survival based on few attributes like gender, age, and social status, we can make very accurate predictions on which passengers would survive. Some groups of people were more likely to survive than others, such as women, children, and the upper-class. Therefore, we can learn about the society priorities and privileges at the time.

## Data Source
Data: https://www.openml.org/data/get_csv/16826755/phpMYEkMl

## Project Description
The objective of the project is to deploy a machine learning pipeline to make a prediction if a passenger in titanic would have survived or not. A short description of the folders is as follows:
  1. titanic_package: Contains scripts for training and testing. 
  2. titanic_api: Contains scripts for deployment as a Web based Rest API(FastAPI).

## App Execution
The app can be started by running the following command:

### tox -r -e run

Note: Please install tox before running the above command. Tox installation can be done as:

### pip install tox==3.25.0
