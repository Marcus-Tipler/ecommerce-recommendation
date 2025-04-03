import random

# ----------------------------------------------------------------
# HOW TO USE
# python SyntheticHistory.py > history.txt
# ----------------------------------------------------------------

def create_matrix(dataOne, dataTwo, dataThree):
    for i in range(dataThree):
        print(f"{random.randint(1, dataOne)} {random.randint(1, dataOne)}")

def main():
    # Change this value according to the synthetic you'd like to create.
    dataOne, dataTwo, dataThree = 500, 500, 600000
    print(f"{dataOne} {dataTwo} {dataThree}")
    create_matrix(dataOne, dataTwo, dataThree)
    
if __name__ == "__main__":
    main()