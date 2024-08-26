from sklearn.datasets import load_iris
iris = load_iris()

X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split

X_train, X_test,y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state = 1)

print("X_train shapes",X_train.shape)
print("X_test shapes",X_test.shape)
print("Y_train shapes",y_train.shape)
print("Y_test shapes",y_test.shape)