# Chat GPT performance on level 5 avoidObstacles

Right out the gate I provided the unparsed question body from the problem, without example or constraints.

https://app.codesignal.com/arcade/intro/level-5/XC9Q2DhRRKQrfLhb5/

```
Human: Hello, who are you?
AI: I am an AI created by OpenAI. How can I help you today?
Human:
Code the following in Python

You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.
AI: This problem can be solved using a greedy algorithm. Here is an example of the code written in Python:

def min_jump_Distance(obstacles):
    # Initialize result (Minimum jump distance)
    min_dist = 0

    # Start loop to traverse through all points
    for i in range(len(obstacles)):
        # If current element is greater than the last element,
        # update min_dist
        if obstacles[i] > min_dist:
            min_dist = obstacles[i]

    return min_dist + 1
```

I updated the prompt to include an example, to which it replied with the same code

```
Example:
For inputArray = [5, 3, 6, 7, 9], the output should be
solution(inputArray) = 4.
```

The code passes one of 12 test cases for the input [2,3] and output 4

Next,

- tuned the language delivery into

- cleaned the test cases

```
Think like an advanced programmer and code a python function named avoidObstacles which solves the following problem.

avoidObstacles  takes an unordered array of integers representing x-coordinates of obstacles situated on a line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles and passes the example test cases below

Examples:
avoidObstacles([5, 3, 6, 7, 9]) = 4

avoidObstacles( [5, 8, 9, 13, 14]) = 15

avoidObstacles([19, 32, 11, 23]) = 33

```

However, the session appeared to give me only slight variations of the same result

After refreshing the sessionI delivered the prompt again, which provided the following answer which is similar

```
def avoidObstacles(arr):

    jump = 0

    for i in range(max(arr)):
        jump += 1
        if all(j % jump != 0 for j in arr): # check if any element of array is divisible by the jump
            return jump

    return jump + 1 # if all elements of array are divisible, then return jump+1.

```

This solution passes 6/6 test cases. However, I would like to understand why the approach and generated variable names changed. My initial thought is that including the function name (which is also the name of the problem) caused this to occur

To test this, I can search a more distinct line from this code and find search results

`https://www.google.com/search?client=firefox-b-1-d&q=all%28j+%25+jump+%21%3D+0+for+j+in+arr%29`

While impressive, this approach wouldn't work for Codesignal interviews. The intro questions are easily searchable but the actual assessment questions are not. I believe they use both steganography and copyright to keep question rotations unindexed, and the time limitations are also intense.

I will continue benchmarking my solutions, my next intention is to have chat GPT benchmark my solutions time & space complexity
