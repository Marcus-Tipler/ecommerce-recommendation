# ----------------------------------------------------------------
# E-commerce recommendation based on item-to-item collaborative 
# filtering, as discussed in the lectures.
# Marcus Francis TIPLER - Computer Science UG Cardiff University.
# ----------------------------------------------------------------


# Importing necessary libraries
import numpy as np
from array import *

# Declarations of global variables

# Defining a function to calculate the cosine similarity between two vectors
# def cosine_similarity(vector1, vector2):
#     dot_product = np.dot(vector1, vector2)
#     magnitude_vector1 = np.linalg.norm(vector1)
#     magnitude_vector2 = np.linalg.norm(vector2)
#     return dot_product / (magnitude_vector1 * magnitude_vector2)

# ----------------------------------------------------------------
# Creates the Purchase History Table matrix.
# ----------------------------------------------------------------
def tablePurchaseHistory():
    history = open('history.txt', 'r')
    dataSummary = history.readline().strip().split()
    amountCustomers = dataSummary[0]
    amountItems = dataSummary[1]
    amountTransactions = dataSummary[2]
    purchaseHistory = np.zeros((int(amountCustomers), int(amountItems)))
    print(purchaseHistory) # TODO: Test Line
    for i in range(int(amountTransactions)-1):
        transaction = history.readline().strip().split(' ')
        user, items = transaction[0], transaction[1]
        purchaseHistory[int(user)-1][int(items)-1] = 1
    print(purchaseHistory) # TODO: Test Line
        
    

# ----------------------------------------------------------------
# Process the input in to lists of vectors
# ----------------------------------------------------------------
def process_input(text):
    item_features = []
    # purchaseHistory = np.zeros
    # purchaseHistory.shape = (4, 4)
    for line in text:
        user, items = line.strip()
        user, items = items.split(' ')

        print(user + " " + items)
        # item_features.append(np.fromstring(line, dtype=float, sep=' '))
    return item_features


# ----------------------------------------------------------------
# Write the output to the command line interface.
# ----------------------------------------------------------------
def write_text(text):
    print(text)


# ----------------------------------------------------------------
# Build the customer-item purchase history table
# ----------------------------------------------------------------
def build_purchase_history_table(item_features):
    pass


# ----------------------------------------------------------------
# Execute the other functions for the core program.
# ----------------------------------------------------------------
def main():
    # item_features = read_text()
    # item_features = process_input(item_features)
    tablePurchaseHistory()

if __name__ == "__main__":
    main()