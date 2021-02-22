import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from tf_utils.dummyData import regression_data


def mean_absolute_error(y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
    return np.mean(np.abs(y_true - y_pred))


def mean_square_error(y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
    return np.mean(np.square(y_true - y_pred))


if __name__ == "__main__":
    x, y = regression_data()
    x = x.reshape(-1, 1)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    regr = LinearRegression()
    regr.fit(x_train, y_train)
    y_pred = regr.predict(x_test)

    r2_score = regr.score(x_test, y_test)
    mae_score = mean_absolute_error(y_test, y_pred)
    mse_score = mean_square_error(y_test, y_pred)

    print(f"R2-Score: {r2_score}")
    print(f"MAE: {mae_score}")
    print(f"MSE: {mse_score}")

    plt.scatter(x, y)
    # plot the train data
    plt.scatter(x_train, y_train,color="g", linewidth=1)
    
    plt.plot(x_test, y_pred, color="r")
    plt.show()
