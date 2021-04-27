# 42 Machine learning project: ft_linear_regression

This first project in the machine learning branch is fairly simple: implementing one of the basic concepts of machine learning, **linear regression**.

Given a set of data, consisting of *mileages of cars* and their *associated prices*, the program trains using gradient descent to find the two variables of the
linear function, **θ0** and **θ1**, that best represents the dataset. The function will then be used to predict the price of any car given its mileage.

The assignment therefore has two main parts: the training program, and the estimation program.

## Specifications

* The whole project was coded using python 3.6.9, and uses the matplotlib library
* Data is stored in csv files
* There are three different programs: training.py, estimation.py and accuracy.py
* Obviously training.py should be run before estimation.py

## Training

The training program uses the data contained in *data.csv* to generate **θ0** and **θ1**, and stores them in a csv file (named "*theta.csv*"). A `-v` option is
available to visualise the data inside a graph, using matplotlib's pyplot.

## Estimation

The estimation program uses *theta.csv*'s computed variables to estimate the price of a car. The mileage is input by the user. A `-v` option is also
available to visualise the data inside a graph, including the user's chosen mileage.

## Accuracy

The accuracy program has a self-explanatory name. The method chosen to calculate the accuracy is the *coefficient of determination*.

## Example of use

```
$> python3 training.py  
$> python3 estimation.py 
Please enter the car's mileage: 10000
The estimated value of this car is 8284 $.
$> python3 accuracy.py 
The coefficient of determination of the linear regression algorithm on the dataset [data.csv] is 0.7329744157937887.
It basically means that the resulting linear function has an accuracy of approx. 73%.
```
