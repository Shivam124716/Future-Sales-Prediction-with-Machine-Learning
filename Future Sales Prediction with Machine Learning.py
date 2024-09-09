import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import plotly.express as px

# Load the dataset
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/advertising.csv")

# Display first 5 rows of the data
print(data.head())

# Check for null values
print(data.isnull().sum())

# Visualization for TV vs Sales
figure = px.scatter(data_frame=data, x="Sales", y="TV", size="TV", trendline="ols")
figure.show()

# Visualization for Newspaper vs Sales
figure = px.scatter(data_frame=data, x="Sales", y="Newspaper", size="Newspaper", trendline="ols")
figure.show()

# Visualization for Radio vs Sales
figure = px.scatter(data_frame=data, x="Sales", y="Radio", size="Radio", trendline="ols")
figure.show()

# Correlation matrix
correlation = data.corr()
print(correlation["Sales"].sort_values(ascending=False))

# Splitting data into features (X) and target (y)
X = np.array(data.drop(["Sales"], axis=1))  # Corrected the deprecation warning
y = np.array(data["Sales"])

# Splitting data into training and testing sets
xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating a linear regression model
model = LinearRegression()

# Fitting the model with training data
model.fit(xtrain, ytrain)

# Displaying the R^2 score of the model on test data
print("Model R^2 score:", model.score(xtest, ytest))

# Making predictions using the model
features = np.array([[230.1, 37.8, 69.2]])  # Example input: TV, Radio, Newspaper
prediction = model.predict(features)

print("Predicted Sales for features [TV=230.1, Radio=37.8, Newspaper=69.2]:", prediction[0])
