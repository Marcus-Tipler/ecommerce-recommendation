# ----------------------------------------------------------------
# E-commerce recommendation based on item-to-item collaborative 
# filtering, as discussed in the lectures.
# Marcus Francis TIPLER - Computer Science UG Cardiff University.
# ----------------------------------------------------------------


# Importing necessary libraries
import numpy as np
from array import *
import math
import os
from statistics import mean 

# Sets the realtime path 
path = os.path.dirname(os.path.realpath(__file__))
pathHistory = os.path.join(path, 'history.txt')
pathQueries = os.path.join(path, 'queries.txt')


# ----------------------------------------------------------------
# Creates the Purchase History Table matrix.
# ----------------------------------------------------------------
def tablePurchaseHistory():
    history = open(pathHistory, 'r')
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


def calculateAngle(x, y):
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    cos_theta = np.dot(x, y) / (norm_x * norm_y)
    theta = math.degrees(math.acos(cos_theta))
    # print(theta)                    # TODO: Test Line
    # print(x)
    # print(y)
    return theta


# ----------------------------------------------------------------
# Creates vectors for each item in the matrix.
# ----------------------------------------------------------------
def createVectors(purchaseHistory, column):
    columnOne = purchaseHistory[:,column]
    return columnOne


def createVectorAverages(purchaseHistory, amountItems):
    vectors = []
    for column in range(int(amountItems)):
        vectors.append(createVectors(purchaseHistory, column))
    return vectors


# ----------------------------------------------------------------
# Creates vectors for each item in the matrix and their averages.
# ----------------------------------------------------------------  
def createVectorAngles(amountItems, vectors):
    angles = []
    anglesDimension = [[90]*int(amountItems)]*int(amountItems)
    for vectorStart in range(int(amountItems)):
        for vectorIterator in range(vectorStart + 1, int(amountItems)):
            anglesDimension[vectorStart][vectorIterator] = calculateAngle(vectors[vectorStart], vectors[vectorIterator])
            # anglesDimension[vectorStart].replace(vectorIterator,12)
            angles.append(anglesDimension[vectorStart][vectorIterator])
            print(f"{anglesDimension[vectorStart][vectorIterator]} ", end="")
        averageAngles = mean(angles)
        print()
    # print(anglesDimension)
    return angles, averageAngles, anglesDimension


def performQuery(angles):
    queries = open(pathQueries, 'r')
    queryLine = queries.readline().strip()
    queryNumbers = []
    for element in queryLine:
        queryNumbers.append(element)
        # print(angles[int(element)])   # TODO: Test Line
    # print(queryNumbers)               # TODO: Test Line

    print(f"Shopping cart:", end="")
    for element in queryNumbers: print(f" {element}", end="")
    print()

    for element in queryNumbers:
        print(f"Item: {element};", end="") # FIXME: needs replacement number for loop after test.
        angleComparator = 90
        angleNumber, angleSaved = 0, 0
        for angle in angles[:][int(element)]:
            angleNumber = angleNumber + 1
            if int(angle) < angleComparator: 
                angleComparator = angle
                angleSaved = angleNumber
        if angleSaved < 90:
            print(f" match: {angleSaved}; angle: {angleComparator}")
                # print(f"SUCCESS IN FUNCTION = {angleSaved} + {angleComparator}")






# ----------------------------------------------------------------
# Execute the other functions for the core program.
# ----------------------------------------------------------------
def main():
    amountCustomers, amountItems, amountTransactions, countPositiveEntries, purchaseHistory = tablePurchaseHistory()
    print(f"Positive entries: {countPositiveEntries}")

    vectors = createVectorAverages(purchaseHistory, amountItems)
    # print(f"Vectors: {vectors}")    # TODO: Test Line

    angles, averageAngles, anglesDimension = createVectorAngles(amountItems, vectors)
    print(f"Average angle: {averageAngles}")
    # print(list_avg)                 # TODO: Test Line
    # print(angles)                   # TODO: Test Line

    # Perform the loop.
    performQuery(anglesDimension)


if __name__ == "__main__":
    main()