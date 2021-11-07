# In-Vehicle Coupon Recommendation Data Set

This data set is present in the UCI Machine Learning Repository, was collected via a survey on Amazon Mechanical Turk and describes different driving scenarios including the destination, current time, weather, passenger, etc., and then ask the person whether he will accept the coupon if he is the driver. In order to solve the problem statement we will use Azure to configure a cloud-based machine learning production model and deploy it. For performing the development of model, we would use Hyper Drive and Auto ML methods. from both the methodology, the model with higest accuary is retrieved (from AutoML and HyerDrive runs) and deployed in cloud with Azure Container Instances(ACI) as a webservice. Authentication is enabled also by enabling the authentication. Once the model is deployed, the behaviour of the endpoint is analysed by getting a response from the service and logs are retrived at the end.

## Dataset

### Overview

**Data Set Information:**

**Number of Features:** 35 features in total. 34 Attributes and 1 Class

**Number of Instances:** 12684

**Class:**
Acceptance feature is used as a class. There are 2 classes in total. These are 0 and 1.

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
*TODO*: Explain the task you are going to be solving with this dataset and the features you will be using for it.

### Access
*TODO*: Explain how you are accessing the data in your workspace.

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
