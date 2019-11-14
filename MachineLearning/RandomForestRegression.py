# as read from GeeksFromGeeks
# https://www.geeksforgeeks.org/random-forest-regression-in-python/

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# load data from csv
data = pd.read_csv("data_random_forest.csv", sep=";")

# read variables from columns
vEquipo = data.iloc[:, 0].values
vPosicion = data.iloc[:, 1].values
vVictorias = data.iloc[:, 2].values
# vVictorias = data.iloc[:, 2].values
vFavor = data.iloc[:, 3].values
vDiferencia = data.iloc[:, 4].values
vValoracion = data.iloc[:, 5:6].values

# define which columns will perform this regression
x = vValoracion
y = vVictorias

print(data.describe())

print("-- Entradas -------")
print("x: ", x)
print("y: ", y)

# Step 4: Fit Random forest regressor to the dataset
# Fitting Random Forest Regression to the dataset

# import the regressor
from sklearn.ensemble import RandomForestRegressor

# create regressor object
regressor = RandomForestRegressor(n_estimators=100, random_state=0)

# fit the regressor with x and y data
regressor.fit(x, y)
print("\r\n")
print("-- Regressor ------")
print(regressor)

x_pred = x
print(x_pred)
y_pred = regressor.predict(x_pred)  # test the output by changing values
print("-- y_pred ------")
print(y_pred)

X_grid = np.arange(min(x), max(x), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))

# Scatter plot for original data
plt.scatter(x, y, color='blue')

# plot predicted data
plt.plot(X_grid, regressor.predict(X_grid), color='green')
plt.title('Random Forest Regression')
plt.xlabel('Valoracion')
plt.ylabel('Victorias')
plt.show()






X_grid = np.arange(min(x), max(x), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))

# Scatter plot for original data
plt.scatter(x, y_pred, color='blue')

# plot predicted data
plt.plot(X_grid, regressor.predict(X_grid), color='green')
plt.title('Random Forest Regression')
plt.xlabel('Valoracion')
plt.ylabel('Victorias Predichas')
plt.show()
