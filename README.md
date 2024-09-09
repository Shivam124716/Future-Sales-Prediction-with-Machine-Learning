Predicting the future sales of a product helps a business manage the manufacturing and advertising cost of the product. There are many more benefits of predicting the future sales of a product. So if you want to learn to predict the future sales of a product with machine learning, this article is for you. In this article, I will take you through the task of future sales prediction with machine learning using Python.
Future Sales Prediction (Case Study)
The dataset given here contains the data about the sales of the product. The dataset is about the advertising cost incurred by the business on various advertising platforms. Below is the description of all the columns in the dataset:

TV: Advertising cost spent in dollars for advertising on TV;
Radio: Advertising cost spent in dollars for advertising on Radio;
Newspaper: Advertising cost spent in dollars for advertising on Newspaper;
Sales: Number of units sold;
So, in the above dataset, the sales of the product depend on the advertisement cost of the product. I hope you now have understood everything about this dataset. Now in the section below, I will take you through the task of future sales prediction with machine learning using Python.
Let’s start the task of future sales prediction with machine learning by importing the necessary Python libraries and the dataset:
Let’s have a look at whether this dataset contains any null values or not:
So this dataset doesn’t have any null values. Now let’s visualize the relationship between the amount spent on advertising on TV and units sold:
Now let’s visualize the relationship between the amount spent on advertising on newspapers and units sold:
Out of all the amount spent on advertising on various platforms, I can see that the amount spent on advertising the product on TV results in more sales of the product. Now let’s have a look at the correlation of all the columns with the sales column:
Now in this section, I will train a machine learning model to predict the future sales of a product. But before I train the model, let’s split the data into training and test sets:
Now let’s train the model to predict future sales:
Now let’s input values into the model according to the features we have used to train it and predict how many units of the product can be sold based on the amount spent on its advertising on various platforms:
Summary
So this is how we can train a machine learning model to predict the future sales of a product. Predicting the future sales of a product helps a business manage the manufacturing and advertising cost of the product. I hope you liked this article on future sales prediction with machine learning. Feel free to ask valuable questions in the comments section below.
