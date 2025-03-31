# ----------------------------------------------------------------
# E-commerce recommendation based on item-to-item collaborative 
# filtering, as discussed in the lectures.
# Marcus Francis TIPLER - Computer Science UG Cardiff University.
# ----------------------------------------------------------------


# Importing necessary libraries
import numpy as np


# Defining a function to calculate the cosine similarity between two vectors
# def cosine_similarity(vector1, vector2):
#     dot_product = np.dot(vector1, vector2)
#     magnitude_vector1 = np.linalg.norm(vector1)
#     magnitude_vector2 = np.linalg.norm(vector2)
#     return dot_product / (magnitude_vector1 * magnitude_vector2)

# ----------------------------------------------------------------
# Read the text file in the current directory.
# ----------------------------------------------------------------
def read_text():
    with open('out.txt', 'r') as file:
        return file.read().splitlines()
    

# ----------------------------------------------------------------
# Process the input in to lists of vectors
# ----------------------------------------------------------------
def process_input(text):
    item_features = []
    for line in text:
        print(line)
        # item_features.append(np.fromstring(line, dtype=float, sep=' '))
    return item_features


# ----------------------------------------------------------------
# Write the output to the command line interface.
# ----------------------------------------------------------------
def write_text(text):
    print(text)


# ----------------------------------------------------------------
# Execute the other functions for the core program.
# ----------------------------------------------------------------
def main():
    item_features = read_text()
    item_features = process_input(item_features)

if __name__ == "__main__":
    main()