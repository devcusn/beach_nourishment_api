import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


class WaveHeightML:
    def __init__(self):
        self.all_data = pd.read_csv('./mock/MOCK_DATA.csv')
        self.data = self.all_data.head(100000)

    def run(self):
        X = np.array([[entry['wind_speed'], entry['water_deep'],
                       entry['wind_impact_duration']] for _, entry in self.data.iterrows()])

        Y = np.array([entry['wave_height']
                     for _, entry in self.data.iterrows()])

        X_train, X_test, y_train, y_test = train_test_split(
            X, Y, test_size=0.6, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f'Mean Squared Error: {mse}')
        new_data = np.array([[35, 25, 2]])
        predicted_wave_height = model.predict(new_data)
        self.res = predicted_wave_height[0]

    def getResult(self):
        return self.res
