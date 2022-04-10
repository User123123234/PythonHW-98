from fileinput import filename
from itertools import count


def countingfunction():
    data_a=open('sample1.txt', "r+")
    data_a_text=data_a.read()
    print(data_a_text)

    data_b=open('sample2.txt',"r+")
    data_b_text=data_b.read()
    print(data_b_text)
    
    data_a.write(data_a_text)
    data_b.write(data_b_text)

countingfunction()