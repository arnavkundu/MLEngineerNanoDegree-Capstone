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