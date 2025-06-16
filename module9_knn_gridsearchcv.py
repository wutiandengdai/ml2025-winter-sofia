import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

class KNNCalculator:


    ### The program asks the user for input N (positive integer) and reads it.
    def dataInput(self):
        while True:
            try: 
                point_size = int(input("Please input a positive integer: "))
                if point_size <= 0 :
                    print("Input value is not positive, please try again.")
                else :
                    return point_size
            except ValueError:
                print("Wrong input, please try agian.")



    ### Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. X and Y are the real numbers.
    def dataInsert(self, size):
        points = np.zeros((size, 2), dtype=np.float32) 
        print(f"Input {size} points. ")

        for i in range(size):
            while True:
                try:
                    x = float(input(f"Input point {i + 1} - X of {size} points(s)"))
                    y = float(input(f"Input point {i + 1} - Y of {size} points(s)"))
                    points[i] = [x, y]
                    break
                except ValueError:
                    print("Wrong input, please try again.")
        return points


target_k = None
accuracy = 0.0


knnCal = KNNCalculator()
print("Input training data set.")
inputN = knnCal.dataInput() 
train_points = knnCal.dataInsert(inputN)
print("Input test data set.")
inputM = knnCal.dataInput()
test_points = knnCal.dataInsert(inputM)


for k in range(1, 10):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(np.array(train_points[:,0]).reshape(-1, 1), np.array(train_points[:,1]))
    y_pred = knn.predict(np.array(test_points[:,0]).reshape(-1, 1))
    acc = accuracy_score(np.array(test_points[:,1]), y_pred)
    print(f"k = {k}, Accuracy = {acc:.4f}")

    if acc > accuracy:
        accuracy = acc
        target_k = k

# Final output
print(f"\nResult: k = {target_k}, Accuracy = {accuracy:.4f}")

        