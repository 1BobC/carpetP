#4:53:13 explaining THE PATTERN
#THE PATTERN... IDIOM
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

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#THE PATTERN / IDIOM  practise... (4:53:13 explaining THE PATTERN)
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

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#Continuing at 4:57:40 with Counting Word Frequency using a Dictionary in funfte.py
# fname = input('Enter filename: ')
# if len(fname) < 1 : fname = 'clown.txt' 
# fhand = open(fname)

# di = dict()
# for lin in fhand:
#     print(lin)
#     lin = lin.rstrip()
#     print(lin)
#     wds = lin.split()    
#     print(wds)
#     for w in wds :
        #print(w)
        #print('***', w, di.get(w, -99))  #near 5:09:00
        # oldcount = di.get(w, 0)         #if the key is not there the count is 0
        # print(w, 'Oldcount', oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount
        #print(w, 'Newcount', newcount)
        # di[w] = di.get(w, 0) + 1         #2nd this code also replaces oldcount etc above idiom: retrieve/create/update counter
        # print(w, 'Newcount', di[w])      #now at 5:15:00
        # if w in di :                          #1st this code replaced by oldcount etc above
        #     di[w] = di[w] + 1
        #     print('*** Already in dic ***')
        # else :
        #     di[w] = 1
        #     print('*** New in dic ***')
        # print(w, di[w])
#print(di)    

#back to dritte for Tuples at 5:23:00    
#But can do more practise here if I want to...  

#from os import getrandom - HOW DID THIS GET HERE??


# fname = input('Enter a filename:  ')
# if len(fname ) < 1: fname = 'romeo.txt'
# fhand = open(fname)

# di = dict()
# for lin in fhand :
#     print(lin)
#     lin = lin.rstrip()
#     print(lin)
#     wds = lin.split()
#     print(wds)
    
#     for w in wds :
#         print(w) 
#         #print('****', w, di.get(w, -99))        # -99 will act as a default value if w not present 
        
#         oldcount = di.get(w, 0)                  # now this line instead with 0
#         print(w, '**oldcount**', oldcount)
        
#         newcount = oldcount + 1
#         di[w] = newcount
#         print(w, 'New count is: ', newcount)
        
#         if w in di :                            # provided this if statement is used
#             di[w] = di[w] + 1
#             print('**Already in dictionary**')
#         else :
#             di[w] = 1
#             print('***New in dictionary***' )
#         #print(w, di[w])
# print(di)
    

#AND ANOTHER PRACTISE THIS TIME READING NOTES AND WATCHING VIDEO EXPLANATION - Wow am impressing myself!

# fname = input('Enter a filename')
# if len(fname) < 1 : fname = 'intro-short.txt'
# ffa = open(fname)

# tots = dict()
# for lin in ffa :
#     #print(lin)
    
#     lin = lin.rstrip()
#     #print(lin)

#     wds = lin.split()
#     #print(wds)
    
#     for w in wds :
#         print(w)
#         #print('Does only default show up?  ',w, tots.get(w, -99))
        
#         if w in tots :
#             tots[w] = tots[w] + 1           
#         else :
#             tots[w] = 1
# #
# print(tots)

# #now onto word with biggest number
# bigcount = None
# bigword = None
# for w, tot in tots.items() :
#     if bigcount is None or tot > bigcount :
#         bigword = w
#         #print(bigword)
#         bigcount = tot
#         #print(bigcount)
# print('The bigword is: ', bigword, 'The big count is: ', bigcount)
    
#NOW DO IT AGAIN !
#name a file
fname = input('Enter a file name:  ')
if len(fname) < 1 : fname = 'clown.txt'
#open it
fhand = open(fname)
#create dictionary
counts = dict()
#lines (for statement)
for lin in fhand :
    #print(lin)
#lines strip right
    lin = lin.rstrip()
    #print(lin)
#split words
    wds = lin.split()
    #print(wds)
#word count
    for w in wds :
        #print(w)
        if w in counts :
            counts[w] = counts[w] + 1
        else :
            counts[w] = 1
#print(counts)
#variables big count & word
bigcount = None
bigword = None
#for statement
for w, count in counts.items() :
    if bigcount is None or count > bigcount :
        bigword = w 
        bigcount = count
print('The bigword is: ', bigword, ' ', 'The bigcount is: ', bigcount)
    

