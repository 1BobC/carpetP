#4:53:13 attempts on THE PATTERN
#THE PATTERN...
# name = input('Enter file: ')
# handle open(name)

# counts = dict()
# for line in handle :
#     words = line.split()
#     for word in words :
#         counts[word] = counts.get(word, 0) + 1
# #basic histogram created, next reveals biggest counts     
# bigcount = None
# bigword = None
# for word, count in counts.items() :
#     if bigcount is None or count > bigcount :
#         bigword = word
#         bigcount = count
        
# print(bigword, bigcount)

fname = input('Enter file: ')       #works ok for clown.txt and words.txt
fhand = open(fname)

counts = dict()
for line in fhand :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1
        print('The wordcounts are: ', counts)
   
bigcount = None
bigword = None
for word, count in counts.items() :
     if bigcount is None or count > bigcount :
         bigword = word
         bigcount = count
        
print('The bigword is: ', bigword, ' The bigcount is: ', bigcount)        

#Continuing at 4:57:40 with Counting Word Frequency using a Dictionary in funfte.py
        
        