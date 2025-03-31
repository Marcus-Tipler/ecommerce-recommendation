# ----------------------------------------------------------------
# E-commerce recommendation based on item-to-item collaborative 
# filtering, as discussed in the lectures.
# Marcus Francis TIPLER - Computer Science UG Cardiff University.
# ----------------------------------------------------------------


# Importing necessary libraries
import numpy as np
from array import *
import math


# ----------------------------------------------------------------
# Creates the Purchase History Table matrix.
# ----------------------------------------------------------------
def tablePurchaseHistory():
    history = open('history.txt', 'r')
    dataSummary = history.readline().strip().split()
    amountCustomers, amountItems, amountTransactions = dataSummary[0], dataSummary[1], dataSummary[2]
    countEntries = 0
    purchaseHistory = np.zeros((int(amountCustomers), int(amountItems)))
    # print(purchaseHistory)        # TODO: Test Line
    for i in range(int(amountTransactions)):
        transaction = history.readline().strip().split(' ')
        user, items = transaction[0], transaction[1]
        if (purchaseHistory[int(user)-1][int(items)-1] == 0):
            countEntries += 1
        purchaseHistory[int(user)-1][int(items)-1] = 1
    # print(purchaseHistory)        # TODO: Test Line
    # print(countEntries)           # TODO: Test Line
    return amountCustomers, amountItems, amountTransactions, countEntries, purchaseHistory


# ----------------------------------------------------------------
# Creates vectors for each item and pre-computes angle definitions.
# ----------------------------------------------------------------
def calculateAverageAngle():

    return 1                        # FIXME: REPLACE 1

def calculateAngle(x, y):
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    cos_theta = np.dot(x, y) / (norm_x * norm_y)
    theta = math.degrees(math.acos(cos_theta))
    print(theta)                    # TODO: Test Line
    return theta


# ----------------------------------------------------------------
# Creates vectors for each item in the matrix.
# ----------------------------------------------------------------
def createVectors(purchaseHistory, column):
    columnOne = purchaseHistory[:,column]
    return columnOne


# ----------------------------------------------------------------
# Execute the other functions for the core program.
# ----------------------------------------------------------------
def main():
    amountCustomers, amountItems, amountTransactions, countPositiveEntries, purchaseHistory = tablePurchaseHistory()
    print(f"Positive entries: {countPositiveEntries}")
    # vectors = createVectors(purchaseHistory, 1)
    # print(f"Vectors: {vectors}")
    # averageAngle = calculateAngle()
    # print(f"Average angle: {averageAngle}")

    vectors, angles = [], []
    for column in range(int(amountItems)):
        vectors.append(createVectors(purchaseHistory, column))
    # print(f"Vectors: {vectors}")  # TODO: Test Line
    for vectorStart in vectors:
        for vectorIterator in vectors:
            angles.append(calculateAngle(vectors[vectorStart], vectors[vectorIterator + vectorStart]))
    print(angles)                   # TODO: Test Line
    

if __name__ == "__main__":
    main()