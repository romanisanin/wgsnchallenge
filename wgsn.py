import unittest

#Test the method max_times_appears
class Test_max_times_appears_method(unittest.TestCase):

    #Test that method returns the value that appears the greatest number of times
    def test_single_value(self):
        excepted = [8]
        actual = max_times_appears([8, 100, 5, -100, 7, 2, 8, 9, 6, 9, 8])
        self.assertEqual(actual, excepted, "Failed. Expected value is {0}, but actual is {1}".format(str(excepted), str(actual)))
    
    #Test that method returns multiple values that appears the greatest number of times
    def test_multiple_values(self):
        excepted = [8, 2, 9]
        actual = max_times_appears([8, 100, 5, -100, 7, 2, 2, 9, 6, 9, 8])
        self.assertEqual(actual, excepted, "Failed. Expected value is {0}, but actual is {1}".format(str(excepted), str(actual)))

    #Test that method returns all values when all values in the array are different
    def test_all_different_numbers(self):
        excepted = [8, 0, 5, -100, 100]
        actual = max_times_appears([8, 0, 5, -100, 100])
        self.assertEqual(actual, excepted, "Failed. Expected value is {0}, but actual is {1}".format(str(excepted), str(actual)))

    #Test that method returns the single value when all values in the array are the same
    def test_all_same_numbers(self):
        excepted = [8]
        actual = max_times_appears([8, 8, 8])
        self.assertEqual(actual, excepted, "Failed. Expected value is {0}, but actual is {1}".format(str(excepted), str(actual)))

    #Test that method returns values without characters when the array contains alphacharacters
    def test_characters_in_array(self):
        excepted = [8]
        actual = max_times_appears([8, "a", 5, -100, 8, 100])
        self.assertEqual(actual, excepted, "Failed. Expected value is {0}, but actual is {1}".format(str(excepted), str(actual)))

    #Test that method returns the single value when all values in the array are the same
    def test_negative_numbers_in_array(self):
        excepted = [-100, 8]
        actual = max_times_appears([-100, 8, -100, 8, 0])
        self.assertEqual(actual, excepted, "Failed. Expected value is {0}, but actual is {1}".format(str(excepted), str(actual)))

        #Test that all numbers from array returns when all the numbers are different
    def test_empty_array(self):
        excepted = []
        actual = max_times_appears([])
        self.assertEqual(actual, excepted, "Failed. Expected value is {0}, but actual is {1}".format(str(excepted), str(actual)))
    


def max_times_appears(array):
    count_dict = {}
    max_list = []
    
    for value in array:
        if str(value).lstrip('-+').isdigit():
            if value not in count_dict:
                count_dict[value] = 1
            else:
                count_dict[value] = count_dict.get(value) + 1
    if len(count_dict) > 1:
        sorted_list = sorted(count_dict.items(), key=lambda x: x[1], reverse = True)
        len_list = len(sorted_list)
        for i in range(len_list - 1):
            if sorted_list[i][1] > sorted_list[i+1][1]:
                max_list.append(sorted_list[i][0])
                break
            else:
                max_list.append(sorted_list[i][0])
                if (i == len_list - 2):
                    max_list.append(sorted_list[i+1][0])
    else:
        max_list = list(count_dict.keys())
    return max_list

if __name__ == '__main__':
    unittest.main()