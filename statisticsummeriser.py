#!/usr/bin/env python3
import math

def load_data(filename):
    """ Takes a string corresponding to a data
        file and returns a list of tuples,each
        containing the subset name and a list of
        floating point data values.

        load_data(str) -> list<tuples<str, list<floats>>>
        """
    file = open(filename, 'r')
    data = []
    for line in file:
        line = line.strip()
        line = line.split(',',1)
        heights = []
        for height in line[1].split(','):
            heights.append(float(height))
        a = line[0], heights
        data.append(a)
    file.close()
    return data
    
    
def get_ranges(data):
    """ Takes a list of floating point numbers
        and returns a tuple with the min and max
        value in the data set.

        get_ranges(list<float>) -> (float, float)
        """
    return min(data), max(data)
        
def get_mean(data):
    """ Returns the mean of the points from a
        list of data.

        get_mean(list<float>) -> float
        """
    mean = sum(data)/len(data)
    return mean

def get_median(data):
    """ Takes a list of data points and returns
        the median value of the data set.

        get_median(list<float>) -> float
    """
    data.sort()
    n = len(data)
    if n % 2 == 0:
        x = int(n/2)
        y = int(n/2-1)
        a = ((data[x])+(data[y]))/2
        return a
    else:
        b = int(n/2)
        return data[b]

def get_std_dev(data):
    """ Returns the standard deviation of data
        points in the data list about the mean.

        get_std_dev(list<float>) -> int
    """
    mean = get_mean(data)
    a = data
    b = []
    for x in a:
        c = x - mean
        c = c ** 2
        b.append(c)
    d = sum(b)/len(a)
    d = math.sqrt(d)
    return d

def display_with_padding(s):
	"""
	Something to print stuff prettily.

	display_with_padding(str) -> None
	
	"""
	print("{0: <15}".format(s), end = '')

def data_summary(data):
    """ Returns a list of tuples containing the
        summary statistics and name of each subset.

        data_summary(list<tuples>) -> list
    """
    summary = []
    for i in data:
        a = i[0], len(i[1]), get_mean(i[1]), get_median(i[1]), min(i[1]), \
            max(i[1]), get_std_dev(i[1])
        summary.append(a)
    return summary

def display_set_summaries(summary):
    """ Displays the summary of information for the
        supplied data set summaries.
        
        display_set_summaries(list<tuples>) ->  str
    """
    words = {0 : 'Count:', 1 : 'Mean:', 2 : 'Median:' , 3 : 'Minimum:' , \
             4 : 'Maximum:', 5 : 'Std Dev:'}
    print('Set Summaries\n')
    display_with_padding('')
    c = 1
    for i in summary:
        display_with_padding(i[0])
    print('')
    for i in words:
        display_with_padding(words[i])
        for i in summary:
            display_with_padding(round(i[c],2))
        c += 1           
        print('')
        
def interact():
    """ Top-level function that defines the text-
        based user interface.

        interact() -> text-based GUI
    """
    print('Welcome to the Statistic Summariser\n')
    data = input('Please enter the data source file: ')
    data = load_data(data)
    while True:
        response = input('\nCommand: ')
        response_splitted = response.split()
        response_list = []
        if response == 'q':
            break
        elif response == 'summary':
            display_set_summaries(data_summary(data))
        elif 'sets' in response_splitted:
            for i in response_splitted[1:]:
                response_list.append(data[int(i)])
            display_set_summaries(data_summary(response_list))
        else:
            print('Unknown command:',response)
     
    

if __name__ == '__main__':
    interact()
