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
...
