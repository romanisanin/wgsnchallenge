#WGSN Code challenge

###The Problem:
Given an array of integers, return the value in the array that appears the greatest number of
times.
For example:
Given the array: [8, 100, 5, -100, 7, 2, 8, 9, 6, 9, 8]
Answer: 8

The solution is written using python 3.6.
Unittest is a unit testing framework which is used for testing purposes in this solution.

To run the application you should have installed python 3.6 or newer, or python online interpreter. 

To run the application with more details use a command with the flag -v: 
`python pathToTheFile\wgsn.py -v`

The method **max_times_appears** returns multiple values that appear the same number of times.

The Class ***Test_max_times_appears_method*** contains 7 tests to check different combinations of array values in the method **max_times_appears**:
1. Test that the method returns the value that appears the greatest number of times
2. Test that the method returns multiple values that appears the greatest number of times
3. Test that the method returns all values when all values in the array are different
4. Test that the method returns the single value when all values in the array are the same
5. Test that the method returns values without characters when the array contains alphacharacters
6. Test that the method returns negative numbers in values when array contains negative numbers in values
7. Test that the method returns empty array when the array is empty

After the test execution is done the report will be generated with the test execution results.
