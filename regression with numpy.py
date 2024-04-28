# Import necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
# Since logistic regression is typically used for binary classification,
# for the sake of simplicity, let's modify the target so we're only predicting
# whether the flower is a Setosa (target == 0) or not.
y_binary = (y == 0).astype(np.int32)
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.2,
random_state=42)
# Initialize the logistic regression model
log_reg = LogisticRegression()
# Train the model
log_reg.fit(X_train, y_train)
# Make predictions
predictions = log_reg.predict(X_test)
# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print(f"Model accuracy: {accuracy:.2f}")