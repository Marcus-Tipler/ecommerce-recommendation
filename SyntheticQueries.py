import random

# ----------------------------------------------------------------
# HOW TO USE
# python SyntheticQueries.py > queries.txt
# ----------------------------------------------------------------

def create_matrix(dataOne, dataTwo, entries):
    for i in range(entries):
        iterator = random.randint(0, 2)
        if iterator == 0:
            print(f"{random.randint(1, dataOne)}")
        if iterator == 1:
            print(f"{random.randint(1, dataOne)} {random.randint(1, dataOne)}")
        if iterator == 2:
            print(f"{random.randint(1, dataOne)} {random.randint(1, dataOne)} {random.randint(1, dataOne)}")

def main():
    # Change this value according to the synthetic you'd like to create.
    entries = 600000
    dataOne, dataTwo = 500, 500
    create_matrix(dataOne, dataTwo, entries)
    
if __name__ == "__main__":
    main()