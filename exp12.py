##register number:21004621
##name: A NAVEEN KUMAR

import sys
with open(sys.argv[1],'r') as f:
    num_words =0
    for i in f:
        word =i.split()
        num_words += len(word)
print("Number of words={}".format(num_words))