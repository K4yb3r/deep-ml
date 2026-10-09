import numpy as np
def linear_regression_normal_equation(X, y):
	
	X, y = np.array(X), np.array(y)

	theta = np.linalg.inv(X.T @ X) @ (X.T @ y)

	return theta