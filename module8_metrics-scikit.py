import numpy as np
from sklearn.metrics import precision_score, recall_score


class SLCalculator:
    inputN = 0
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


    ### Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. X and Y are the real numbers.
    def dataInsert(self):
        self.points = np.zeros((self.inputN, 2), dtype=np.float32) 
        print(f"Input {self.inputN} points. ")

        for i in range(self.inputN):
            while True:
                try:
                    x = float(input(f"Input point {i + 1} - X of {self.inputN} points(s), 0 or 1 "))
                    y = float(input(f"Input point {i + 1} - Y of {self.inputN} points(s), 0 or 1 "))
                    self.points[i] = [x, y]
                    break
                except ValueError:
                    print("Wrong input, please try again.")

    ### In the end, the program asks the user for input X and outputs: the result (Y) of k-NN Regression if k <= N, or any error message otherwise.
    def dataProcess(self):
        # Convert to NumPy arrays
        true_labels = np.array(self.points[:,0])
        pred_labels = np.array(self.points[:,1])

        # Compute precision and recall using scikit-learn
        precision = precision_score(true_labels, pred_labels)
        recall = recall_score(true_labels, pred_labels)
        print(f"\nPrecision: {precision:.4f}")
        print(f"Recall:    {recall:.4f}")
        
slCal = SLCalculator()
slCal.dataInput()
slCal.dataInsert()
slCal.dataProcess()

