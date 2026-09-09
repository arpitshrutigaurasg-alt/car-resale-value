import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score, mean_squared_error

X = np.array([
    [1, 12000, 1000, 1],
    [2, 18000, 1200, 1],
    [3, 25000, 1500, 1],
    [2, 30000, 1200, 1],
    [4, 35000, 1500, 2],
    [3, 40000, 1800, 1],
    [5, 45000, 1200, 2],
    [2, 22000, 1600, 1],
    [4, 50000, 1800, 2],
    [6, 60000, 1200, 2],

    [1, 15000, 1400, 1],
    [2, 28000, 1500, 1],
    [3, 32000, 1800, 1],
    [5, 55000, 1500, 2],
    [4, 42000, 2000, 1],
    [6, 70000, 1200, 2],
    [7, 80000, 1500, 3],
    [3, 38000, 1600, 1],
    [2, 20000, 1800, 1],
    [5, 65000, 1800, 2],

    [1, 10000, 1200, 1],
    [3, 27000, 1400, 1],
    [4, 48000, 1500, 2],
    [6, 72000, 1800, 2],
    [7, 90000, 1200, 3],
    [2, 24000, 2000, 1],
    [5, 58000, 1600, 2],
    [4, 36000, 1800, 1],
    [3, 45000, 1200, 2],
    [8, 100000, 1500, 3],

    [1, 14000, 1800, 1],
    [2, 26000, 1200, 1],
    [4, 40000, 2000, 1],
    [5, 62000, 1500, 2],
    [6, 68000, 1800, 2],
    [3, 30000, 2000, 1],
    [7, 85000, 1500, 3],
    [4, 52000, 1600, 2],
    [2, 19000, 1400, 1],
    [5, 70000, 2000, 2],

    [1, 8000, 1000, 1],
    [3, 35000, 1500, 1],
    [4, 46000, 1800, 2],
    [6, 75000, 1200, 2],
    [8, 105000, 1500, 3],
    [2, 21000, 1600, 1],
    [5, 50000, 1800, 2],
    [3, 28000, 1200, 1],
    [7, 95000, 2000, 3],
    [4, 44000, 1500, 2]
])


y = np.array([
    10.5, 9.2, 8.1, 8.5, 6.9,
    8.8, 5.8, 9.8, 7.2, 5.0,
    11.8, 8.7, 9.0, 5.9, 6.4,
    4.8, 3.8, 8.2, 10.2, 5.7,
    12.5, 8.9, 6.8, 5.2, 3.5,
    10.8, 5.9, 7.6, 6.5, 3.0,
    11.5, 8.5, 9.8, 5.6, 5.1,
    8.9, 3.9, 6.8, 9.6, 6.2,
    13.2, 8.0, 6.5, 4.9, 3.2,
    10.1, 5.8, 8.7, 3.6, 6.9
])

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

poly = PolynomialFeatures(degree=2)

X_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

model = Ridge(alpha=1)

model.fit(X_poly, y_train)

train_data = model.predict(X_poly)
train_score = r2_score(y_train, train_data)

test_data = model.predict(X_test_poly)
test_score = r2_score(y_test, test_data)

mae = mean_squared_error(y_test,test_data)
mse = mean_squared_error(y_test,test_data)

print("Model trained successfully!")
print(f"Train Score: {train_score:.4f}")
print(f"Test Score: {test_score:.4f}")
print(f"MAE :- {mae}")
print(f"MSE :- {mse}")