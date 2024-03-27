import unittest
from app import app
from modelBuild import melbourne_data, melbourne_features
import pandas as pd
import joblib

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_predict_endpoint(self):
        sample_data = {
            'Rooms': 3,
            'Bathroom': 2,
            'Landsize': 300,
            'Lattitude': -37.81,
            'Longtitude': 144.98
        }
        response = self.app.post('/predict', json=sample_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('predicted_price', response.json)

class TestModel(unittest.TestCase):
    def setUp(self):
        # Load the trained model
        self.model = joblib.load('melbourne_house_price_model.pkl')

    def test_model_prediction(self):
        # Create sample input data
        sample_data = {
            'Rooms': 3,
            'Bathroom': 2,
            'Landsize': 300,
            'Lattitude': -37.81,
            'Longtitude': 144.98
        }
        sample_df = pd.DataFrame([sample_data])

        # Make prediction
        prediction = self.model.predict(sample_df)

        # Check if prediction is within reasonable bounds
        self.assertTrue(prediction > 0)  # Price should be positive

    def test_model_training(self):
        # Check if the model was trained successfully
        self.assertIsNotNone(self.model)  # Model should not be None
        self.assertTrue('Price' in melbourne_data.columns)  # 'Price' column should be present
        self.assertEqual(len(melbourne_features), 5)  # Expected number of features

if __name__ == '__main__':
    unittest.main()
