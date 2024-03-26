# Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load the dataset
melbourne_file_path = './dataset/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

# Drop missing values
melbourne_data = melbourne_data.dropna(axis=0)

# Selecting features and target variable
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]
y = melbourne_data['Price']

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f"Training score: {train_score}")
print(f"Testing score: {test_score}")

# Save the model
joblib.dump(model, 'melbourne_house_price_model.pkl')
