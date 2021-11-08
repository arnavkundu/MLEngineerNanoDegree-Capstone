# In-Vehicle Coupon Recommendation Data Set

This data set is present in the UCI Machine Learning Repository, was collected via a survey on Amazon Mechanical Turk and describes different driving scenarios including the destination, current time, weather, passenger, etc., and then ask the person whether he will accept the coupon if he is the driver. In order to solve the problem statement we will use Azure to configure a cloud-based machine learning production model and deploy it. For performing the development of model, we would use Hyper Drive and Auto ML methods. from both the methodology, the model with higest accuary is retrieved (from AutoML and HyerDrive runs) and deployed in cloud with Azure Container Instances(ACI) as a webservice. Authentication is enabled also by enabling the authentication. Once the model is deployed, the behaviour of the endpoint is analysed by getting a response from the service and logs are retrived at the end.

## Dataset

### Overview

**Data Set Information:**

**Number of Features:** 35 features in total. 34 Attributes and 1 Class

**Number of Instances:** 12684

**Class:**
Acceptance feature is used as a class. There are 2 classes in total. These are 0 and 1. Performing some EDA we see that the target class is a balanced one.

**Attribute Information:**

- destination: No Urgent Place, Home, Work
- passanger: Alone, Friend(s), Kid(s), Partner (who are the passengers in the car)
- weather: Sunny, Rainy, Snowy
- temperature:55, 80, 30
- time: 2PM, 10AM, 6PM, 7AM, 10PM
- coupon: Restaurant(<$20), Coffee House, Carry out & Take away, Bar, Restaurant($20-$50)
- expiration: 1d, 2h (the coupon expires in 1 day or in 2 hours)
- gender: Female, Male
- age: 21, 46, 26, 31, 41, 50plus, 36, below21
- maritalStatus: Unmarried partner, Single, Married partner, Divorced, Widowed
- has_Children:1, 0
- education: Some college - no degree, Bachelors degree, Associates degree, High School Graduate, Graduate degree (Masters or Doctorate), Some High School
- occupation: Unemployed, Architecture & Engineering, Student,
- Education&Training&Library, Healthcare Support,
- Healthcare Practitioners & Technical, Sales & Related, Management,
- Arts Design Entertainment Sports & Media, Computer & Mathematical,
- Life Physical Social Science, Personal Care & Service,
- Community & Social Services, Office & Administrative Support,
- Construction & Extraction, Legal, Retired,
- Installation Maintenance & Repair, Transportation & Material Moving,
- Business & Financial, Protective Service,
- Food Preparation & Serving Related, Production Occupations,
- Building & Grounds Cleaning & Maintenance, Farming Fishing & Forestry
- income: $37500 - $49999, $62500 - $74999, $12500 - $24999, $75000 - $87499,
- $50000 - $62499, $25000 - $37499, $100000 or More, $87500 - $99999, Less than $12500
- Bar: never, less1, 1 ~ 3, gt8, nan4 ~ 8 (feature meaning: how many times do you go to a bar every month?)
- CoffeeHouse: never, less1, 4 ~ 8, 1 ~ 3, gt8, nan (feature meaning: how many times do you go to a coffeehouse every month?)
- CarryAway:n4~8, 1 ~ 3, gt8, less1, never (feature meaning: how many times do you get take-away food every month?)
- RestaurantLessThan20: 4 ~ 8, 1~3, less1, gt8, never (feature meaning: how many times do you go to a restaurant with an average expense per person of less than $20 every month?)
- Restaurant20To50: 1~3, less1, never, gt8, 4 ~ 8, nan (feature meaning: how many times do you go to a restaurant with average expense per person of $20 - $50 every month?)
- toCoupon_GEQ15min:0,1 (feature meaning: driving distance to the restaurant/bar for using the coupon is greater than 15 minutes)
- toCoupon_GEQ25min:0, 1 (feature meaning: driving distance to the restaurant/bar for using the coupon is greater than 25 minutes)
- direction_same:0, 1 (feature meaning: whether the restaurant/bar is in the same direction as your current destination)
- direction_opp:1, 0 (feature meaning: whether the restaurant/bar is in the same direction as your current destination)

### Overview
This data set is present in the UCI Machine Learning Repository, was collected via a survey on Amazon Mechanical Turk and describes different driving scenarios including the destination, current time, weather, passenger, etc., and then ask the person whether he will accept the coupon if he is the driver.

- **Dataset info link:** https://archive.ics.uci.edu/ml/datasets/in-vehicle+coupon+recommendation
- **Dataset link:** https://archive.ics.uci.edu/ml/machine-learning-databases/00603/in-vehicle-coupon-recommendation.csv

### Task
In this project we will try to predict if a set of attributes will encourage an acceptance of coupon if he is a driver. There are different set of attributes, mostly categorical or boolean through which a condition will be set which with either favour acceptance or rejection. For the task of MLOps we will use AutoML and Hyperdrive to understand what model would be able to predict with highest accuracy and finally deploy it for everyone to use. We will also test if with a set of JSON, our prediction is correct or not.

### Access
In terms of access, we will use the URL of the **Dataset link** to save the same in a tabular web file.

## Automated ML

AutoMLConfig Class represents configuration for submitting an automated ML experiment in Azure Machine Learning. This configuration object contains and persists the parameters for configuring the experiment run, as well as the training data to be used at run time. In this experiment we used the following configuration:

![image](https://user-images.githubusercontent.com/38326274/140656086-f2c7722c-639c-4369-acdc-d1d3bd0d172f.png)

Following are some key conifgs for this run. The taks that needs to be performed is set as classification with the dataset being passed to the training data. The column that needs to be trated as a target variable is mentioned as "Y". In this taks we have also enable early stopping (enabling the early termination, the run terminates if the score is not improving in the short term). Finally we also set a log file to log all the errors that might occur during the run, so that we can use them to debug, in case required.


### Results
The best AutoML model obtained an accuracy of 77.3% (Voting Ensemble), but considering that it is based on a software decision and the Best Hyperdrive model obtained an accuracy of approx. 66.7%, we can assume that the AutoML model has a higher grade result. Parameters for the modelling are the same attributes that were provided in the dataset. In terms of improving the model, we can think of more feature engineering like creation of more meaningful features, or feature reduction due to high correlation. In cases of classification, we understand that it is not only accuracy that determines the goodness of the model and we could have looked into the F1-score or Precision or recall depending on the need of the problem statement.

- **Screenshot 1:** RunDetails Widget 
![image](https://user-images.githubusercontent.com/38326274/140769076-a20a10f6-9f16-4882-9f99-b14c6d7284e4.png)

- **Screenshot 2:** Best Run details
![image](https://user-images.githubusercontent.com/38326274/140769339-dd99a42a-d264-4783-a6a3-9dd1b60cdf96.png)
*******************************************************************************************************************************************************************
![image](https://user-images.githubusercontent.com/38326274/140769453-b66b557e-7916-441a-9833-46b475bb8dd7.png)

## Hyperparameter Tuning
Automate efficient hyperparameter tuning by using Azure Machine Learning HyperDrive package. In this package we tune hyperparameters with the Azure Machine Learning SDK. For this task we have used Logistic Regression. Logistic regression is applied to predict the categorical dependent variable. In other words, it's used when the prediction is categorical, for example, yes or no, true or false, 0 or 1. Logistic regression is easier to train and implement as compared to other methods and hence was the first choice so Hyperparameter tuning.

## Hyperparmeters
### Parameters
- '--C' : choice(0.001,0.01,0.1,1.0,10.0,50.0,100,1000), (Discrete choices: Inverse of regularization strength. Smaller values cause stronger regularization)
- '--max_iter': choice(10,25) (Discrete choices: Maximum number of iterations to converge)

### Early Termination Policy:

- BanditPolicy
- slack_factor = 0.1
- evaluation_interval = 1
- delay_evaluation = 5

### HyperDrive Configuration

- Primary metric: "Accuracy"
- Max total runs: 100
- Max concurrent runs: 5

### Results
The best HyperDrive model obtained 66.7% accuracy, trained with logistic regression, Regularization Strength = 100 and maximum iterations = 10. Inspiration from the 77% accuracy of the AutoML model and looking at the type of variables in the dataset (Mostly categorical), the Hyperdrive model could be improved by choosing a more robust algorithm, such as Random Forest Classifier (For Example CatBoost) or Voting Esemble Classifier (As inspired from AutoML run).

- **Screenshot 3:**: Rundetails Widget for Hyperdrive
![image](https://user-images.githubusercontent.com/38326274/140718297-aac6f3aa-f2c9-44b2-ba61-fa80d19b63c4.png)


- **Screenshot 4:**: Best Model
![image](https://user-images.githubusercontent.com/38326274/140718448-989eb92c-3022-4fa6-9d79-189ee060bb75.png)

## Model Deployment
AutoML’s best model accuracy = 77.3%

HyperDrive’s best model accuracy = 66.67%

Looking at the wide difference in the best model from AutoML and Hyperdrive, it was decided to deploy the AutoML model. To carry on the task, we first register the model. Then the environment along with the inference is created making sure that the conda dependencies is loaded. The score.py file contians the initialization and exit functions for the best model that is deployed. The deployment of model is through **Azure Container instance (ACI)** with configurations: cpu_cores=1, memory_gb=1.

- **Screenshot 5: Model Registration**
##### AutoML Registration
![image](https://user-images.githubusercontent.com/38326274/140729723-409adb5c-23b5-452f-afb9-f4ddc7cae760.png)
*************************************************************************************************************************************************************************
![image](https://user-images.githubusercontent.com/38326274/140729633-242c3ba4-1107-4ae7-9302-b7c3b8f68879.png)

##### Hyperdrive Model registration
![image](https://user-images.githubusercontent.com/38326274/140731710-16fab851-602d-4c35-87c3-e207bcd917bb.png)


- **Screenshot 6: Model Deployment**
![image](https://user-images.githubusercontent.com/38326274/140730102-3cf8eef0-f832-4582-b7de-168a18f0e998.png)
*************************************************************************************************************************************************************************
![image](https://user-images.githubusercontent.com/38326274/140729945-b43a3962-095c-4f5d-838f-b4e9068da1dd.png)


- **Screenshot 7: Model Endpoint Active**

    ![image](https://user-images.githubusercontent.com/38326274/140750052-26cb73b5-0067-4690-8fb4-273eecaa9a19.png)


- **Screenshot 8: Testing the Model Endpoint**
![image](https://user-images.githubusercontent.com/38326274/140703399-1ae41fc2-b957-4821-8abf-a0df0a8e264b.png)


## Screen Recording
![Screen Cast for Capstone Project](https://vimeo.com/643549473)
