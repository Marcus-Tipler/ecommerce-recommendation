# ----------------------------------------------------------------
# E-commerce recommendation based on item-to-item collaborative 
# filtering, as discussed in the lectures.
# Marcus Francis TIPLER - Computer Science UG Cardiff University.
# ----------------------------------------------------------------


# Importing necessary libraries
import numpy as np
from array import *


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
    return countEntries


def calculateAverageAngle():
    return 1


# ----------------------------------------------------------------
# Execute the other functions for the core program.
# ----------------------------------------------------------------
def main():
    # item_features = read_text()
    # item_features = process_input(item_features)
    countPositiveEntries = tablePurchaseHistory()
    print(f"Positive entries: {countPositiveEntries}")
    averageAngle = calculateAverageAngle()
    print(f"Average angle: {averageAngle}")

if __name__ == "__main__":
    main()