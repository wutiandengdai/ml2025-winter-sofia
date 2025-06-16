import numpy as np
from sklearn.neighbors import KNeighborsRegressor

class KNNCalculator:

    inputN = 0
    k = 0
    points = None

    ### The program asks the user for input N (positive integer) and reads it.
    def dataInput(self):
        while True:
            try: 
                self.inputN = int(input("Please input a positive integer: "))
                if self.inputN <= 0 :
                    print("Input value is not positive, please try again.")
                else :
                    break
            except ValueError:
                print("Wrong input, please try agian.")

    ### Then the program asks the user for input k (positive integer) and reads it.
    def dataInit(self):
        while True:
            try: 
                self.k = int(input("Please input a positive integer for parameter k of kNN algorithm: "))
                if self.k <= 0 :
                    print("Input value is not positive, please try again.")
                else :
                    break
            except ValueError:
                print("Wrong input, please try agian.")

    ### Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. X and Y are the real numbers.
    def dataInsert(self):
        self.points = np.zeros((self.inputN, 2), dtype=np.float32) 
        print(f"Input {self.inputN} points. ")

        for i in range(self.inputN):
            while True:
                try:
                    x = float(input(f"Input point {i + 1} - X of {self.inputN} points(s)"))
                    y = float(input(f"Input point {i + 1} - Y of {self.inputN} points(s)"))
                    self.points[i] = [x, y]
                    break
                except ValueError:
                    print("Wrong input, please try again.")

    ### In the end, the program asks the user for input X and outputs: the result (Y) of k-NN Regression if k <= N, or any error message otherwise.
    def dataProcess(self, inputX):
        if(self.k > self.inputN):
            print("k should be no larger than N.")
            raise ValueError
        
        # Show variance of y
        variance = np.var(np.array(self.points[:,1]))
        print(f"Variance of labels (y): {variance:.4f}")

        knn = KNeighborsRegressor(n_neighbors=self.k)
        knn.fit(np.array(self.points[:,0]).reshape(-1, 1), np.array(self.points[:,1]))

        # Predict and show result
        y_pred = knn.predict(np.array(inputX).reshape(-1, 1))
        print(f"Predicted Y for X = {inputX}: {y_pred[0]:.4f}")
        
        return y_pred

        
knnCal = KNNCalculator()
knnCal.dataInput()
knnCal.dataInit()
knnCal.dataInsert()

while True:
    try: 
        inputX = int(input("Please input x of prediction point: "))
        break;
    except ValueError:
        print("Wrong input, please try agian.")
    
predictY = knnCal.dataProcess(inputX)
print(predictY)

