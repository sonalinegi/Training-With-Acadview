#FILE HANDLING
# Write a Python program to read last n lines of a file
fn='test.txt'
with open(fn,'r') as f :
    lines = f.readlines()
N=2
for i in range(len(lines)-N,len(lines)) :
    print(lines[i])

#Write a Python program to count the frequency of words in a file.
#one way to count freq of words by importing counter
from collections import Counter
file=open('test2.txt','r')
def word_count(file):
        with open(file) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("test2.txt"))

#other way of counting
file=open('test2.txt','r+')
wordcount={}
for word in file.read().split():
    if word  in wordcount:
        wordcount[word] += 1
    else:
        wordcount[word] = 1
for k,v in wordcount.items():
    print(k, v)

# Write a Python program to copy the contents of a file to another file
with open('old.txt','r') as f:
    with open('new.txt','r+') as f1 :
        for line in f:
            f1.write(line)


#Write a Python program to combine each line from first file with the corresponding line in second file.

 with open('test.txt') as f, open('test2.txt') as f1:
    for line1, line2 in zip(f, f1):
        # line1 from abc.txt, line2 from test.txt
        print(line1 + line2)


