from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory
from sklearn.model_selection import train_test_split
from azureml.core import Workspace, Dataset, Run


try:
    run  = Run.get_context()
    workspace = run.experiment.workspace
except:
    workspace = Workspace.from_config()

dataset = Dataset.get_by_name(workspace, name='in-vehicle-coupon-reco')
ds = dataset.to_pandas_dataframe()

def clean_data(data):

    # Clean and one hot encode data
    x_df = data.dropna()
    
    destinations = pd.get_dummies(x_df.destination, prefix="destination")
    x_df.drop("destination", inplace=True, axis=1)
    x_df = x_df.join(destinations)
    
    passangers = pd.get_dummies(x_df.passanger, prefix="passanger")
    x_df.drop("passanger", inplace=True, axis=1)
    x_df = x_df.join(passangers)
    
    weathers = pd.get_dummies(x_df.weather, prefix="weather")
    x_df.drop("weather", inplace=True, axis=1)
    x_df = x_df.join(weathers)
    
    temperature = pd.get_dummies(x_df.temperature, prefix="temperature")
    x_df.drop("temperature", inplace=True, axis=1)
    x_df = x_df.join(temperature)
    
    time = pd.get_dummies(x_df.time, prefix="time")
    x_df.drop("time", inplace=True, axis=1)
    x_df = x_df.join(time)
    
    coupon = pd.get_dummies(x_df.coupon, prefix="coupon")
    x_df.drop("coupon", inplace=True, axis=1)
    x_df = x_df.join(coupon)

    age = pd.get_dummies(x_df.age, prefix="age")
    x_df.drop("age", inplace=True, axis=1)
    x_df = x_df.join(age)
    
    maritalStatus = pd.get_dummies(x_df.maritalStatus, prefix="maritalStatus")
    x_df.drop("maritalStatus", inplace=True, axis=1)
    x_df = x_df.join(maritalStatus)
    
    education = pd.get_dummies(x_df.education, prefix="education")
    x_df.drop("education", inplace=True, axis=1)
    x_df = x_df.join(education)
    
    occupation = pd.get_dummies(x_df.occupation, prefix="occupation")
    x_df.drop("occupation", inplace=True, axis=1)
    x_df = x_df.join(occupation)
    
    income = pd.get_dummies(x_df.income, prefix="income")
    x_df.drop("income", inplace=True, axis=1)
    x_df = x_df.join(income)
    
    Bar = pd.get_dummies(x_df.Bar, prefix="Bar")
    x_df.drop("Bar", inplace=True, axis=1)
    x_df = x_df.join(Bar)
    
    CoffeeHouse = pd.get_dummies(x_df.CoffeeHouse, prefix="CoffeeHouse")
    x_df.drop("CoffeeHouse", inplace=True, axis=1)
    x_df = x_df.join(CoffeeHouse)
    
    CarryAway = pd.get_dummies(x_df.CarryAway, prefix="CarryAway")
    x_df.drop("CarryAway", inplace=True, axis=1)
    x_df = x_df.join(CarryAway)
    
    RestaurantLessThan20 = pd.get_dummies(x_df.RestaurantLessThan20, prefix="RestaurantLessThan20")
    x_df.drop("RestaurantLessThan20", inplace=True, axis=1)
    x_df = x_df.join(RestaurantLessThan20)
    
    Restaurant20To50 = pd.get_dummies(x_df.Restaurant20To50, prefix="Restaurant20To50")
    x_df.drop("Restaurant20To50", inplace=True, axis=1)
    x_df = x_df.join(Restaurant20To50)
    
    
    x_df["expiration"] = x_df.expiration.apply(lambda s: 1 if s == "1d" else 0)
    x_df["gender"] = x_df.gender.apply(lambda s: 1 if s == "Male" else 0)
    
    #Removing car as this is a variable with > 99% missing values
    if 'car' in list(data.columns):
        x_df = x_df.drop(['car'], axis=1)
    y_df = x_df.pop("Y")
    
    return x_df,y_df

def main():
    
    x, y = clean_data(ds)
    # TODO: Split data into train and test sets.
    x_train, x_test, y_train,y_test = train_test_split(x,y, test_size=0.3, random_state=279)
    
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))

if __name__ == '__main__':
    main()