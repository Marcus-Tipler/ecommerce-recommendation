# E-Commerce Recommendation Program
Amazon, eBay, and many other E-Commerce platforms recommend products to you in one form or another. A good way of doing this is by looking at the purchases of everyone on your website and understanding the relation between products. To do this, we can create angles based on wether or not customers purchased an item or not. The lower the angle, the more likely it relates to the current customer. In this Python Program, we aim to achieve the calculation of these angles in advance and make it viewable to a consumer.

# How-To use
It's simple enough to use, all you have to do to test the program by itself is the following:
### Step 1
Open the command line (or terminal) on any given device and in your directory of choice, type:
```cli
git clone https://github.com/Marcus-Tipler/ecommerce-recommendation.git
```
### Step 2
In this given example, place your data or the simulated data in the same repository as the python file, and make sure that the files are called 'history.txt' and 'queries.txt'.

### Step 3
Then type the following:
```cli
python Recommend.py
```
And the program will pre-calculate all of the relations between purchases and print the recommendations in the command line interface.
Alternatively, you could type the following:
```cli
python Recommend.py > output.txt
```
and the data will appear in a text file named 'output.txt' in your given directory.

# Synthetic and Test Data Creation
The creation of synthetic data is made simple thanks to the use of the 'SyntheticQueries.py' and 'SyntheticHistory.py' files. These were not mandatory but were made to test the runtime of my application.
There are three adjustable variables for each file.
### Synthetic History properties
On the subject of Synthetic History data, we have three variables.
1. Data 1: Number of simulated customers.
2. Data 2: Number of simulated items on the store.
3. Data 3: Number of simulated transactions.
These can each be re-written to be any simulated data that you would like.

### Synthetic Queries properties
On the subject of Synthetic Queries data, we have three variables.
1. Entries: the number of simulated carts.
2. Data 1: Number of simulated customers.
3. Data 2: Number of simulated items on the store.
These can each be re-written to be any simulated data that you would like.

# Functions Used
For the calculation of the Angle, a function was used from my University Coursework:
```python
def calculateAngle(x, y):
	norm_x = np.linalg.norm(x)
	norm_y = np.linalg.norm(y)
    cos_theta = np.dot(x, y) / (norm_x * norm_y)
	theta = math.degrees(math.acos(cos_theta))
    return theta
```
This function allowed us to create an angle from multiple vectors. Each vector (called 'x' and 'y' respectively) are lists of boolean types that determine whether or not the product has been purchased for each customer on the website.
NumPy (np here), was used to calculate these angles and the angles were then turned in to degrees using the math.degrees function.

To create the individual vectors:
```python
def createVectors(purchaseHistory, column):
    columnOne = purchaseHistory[:,column]
    return columnOne
```
```python
def createVectorAverages(purchaseHistory, amountItems):
    vectors = []
    for column in range(int(amountItems)):
        vectors.append(createVectors(purchaseHistory, column))
    return vectors
```
These functions allowed me to create individual 'lists' of boolean types to be iterated through for the angle calculations:
```python
def createVectorAngles(amountItems, vectors):
    angles = []
    anglesDimension = [[90.00]*int(amountItems)]*int(amountItems)
    anglesMap = np.array(anglesDimension)
    for vectorStart in range(int(amountItems)):
        for vectorIterator in range(vectorStart + 1, int(amountItems)):
            anglesMap[vectorStart][vectorIterator] = calculateAngle(vectors[vectorStart], vectors[vectorIterator])
            anglesMap[vectorIterator][vectorStart] = anglesMap[vectorStart][vectorIterator]
            
            angles.append(anglesMap[vectorStart][vectorIterator])
    averageAngles = mean(angles)
    return angles, averageAngles, anglesMap
```
This function calculated the angles, added them to a list and made the average of all the angles to comply with coursework regulations. The angles were also added to a map with their respective coordinates 'vectorStart' and 'vectorIterator' (also known as 'x' and 'y'). This made it easy to find the required down the line.

And finally:
```python
while True:
	...

	if queryLine == []:
        break

	...

	recommend = {}
        for element in queryNumbers:
            print(f"Item: {element}", end="")
            angleComparator = 90
            angleNumber, angleSaved = 0, 0
            visibleArray = angles[int(element) - 1, :]
            for angle in visibleArray:
                angleNumber = angleNumber + 1
                if float(angle) < angleComparator: 
                    if str(angleNumber) not in queryNumbers:
                        angleComparator = angle
                        angleSaved = angleNumber
            if angleComparator < 90:
                print(f"; match: {angleSaved}; angle: {"{:.2f}".format(angleComparator, 2)}")
                # recommend.append({angleSaved, angleComparator})
                recommend["{:.2f}".format(angleComparator)] = angleSaved
            else: print(f" no match")

        print("Recommend:", end="")
        recommend = sorted(recommend.items())
        for x, y in recommend:
            print(f" {y}", end="")
        print()
```
This function made the recommendations. Firstly it detects whether or not the item has any relevance whatsoever and then it adds it's angle and it's numeric value to a list of dictionaries.
This can then be iterated through and sorted for an organised output that displays the top recommended product for that particular customer.