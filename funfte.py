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

# fname = input('Enter file: ')       #works ok for clown.txt and words.txt
# fhand = open(fname)

# counts = dict()
# for line in fhand :
#     words = line.split()
#     for word in words :
#         counts[word] = counts.get(word, 0) + 1
#         print('The wordcounts are: ', counts)
   
# bigcount = None
# bigword = None
# for word, count in counts.items() :
#      if bigcount is None or count > bigcount :
#          bigword = word
#          bigcount = count
        
# print('The bigword is: ', bigword, ' The bigcount is: ', bigcount)        

#Continuing at 4:57:40 with Counting Word Frequency using a Dictionary in funfte.py
fname = input('Enter filename: ')
if len(fname) < 1 : fname = 'clown.txt' 
fhand = open(fname)

di = dict()
for lin in fhand:
    print(lin)
    lin = lin.rstrip()
    print(lin)
    wds = lin.split()    
    print(wds)
    for w in wds :
        #print(w)
        #print('***', w, di.get(w, -99))  #near 5:09:00
        # oldcount = di.get(w, 0)         #if the key is not there the count is 0
        # print(w, 'Oldcount', oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount
        #print(w, 'Newcount', newcount)
        di[w] = di.get(w, 0) + 1         #2nd this code also replaces oldcount etc above idom: retrieve/create/update counter
        print(w, 'Newcount', di[w])      #now at 5:15:00
        # if w in di :                          #1st this code replaced by oldcount etc above
        #     di[w] = di[w] + 1
        #     print('*** Already in dic ***')
        # else :
        #     di[w] = 1
        #     print('*** New in dic ***')
        # print(w, di[w])
print(di)    

#back to dritte for Tuples at 5:23:00                                  
        