#4:17:56 The Guardian Pattern
han = open('mbox-short.txt')

for line in han :
    line = line.rstrip()
    #print('line: ', line)       #add a third line 
    # if line == "" :                 #second Guardian line
    #     print('Skip blank')         #second Guardian line
    #     continue                    #second Guardian line
    
    wds = line.split()
    #print('Words: ', wds)       #add line to find out something before Traceback line (run to see result)
    #if len(wds) < 1 : continue     #first Guardian line and comment out all debug lines
    #if len(wds) < 1 : continue      #Strengthening the Guardian if line Has From but no other words 
    #if wds[0] != 'From' :       #shows Traceback but also result of Sat ??
    if len(wds) < 3 or wds[0] != 'From' :   #FINALLY compound the Guardian!!
                                            #NB try reversing the order and it FAILs - the Guardian must come first!!
        #print('Ignore')         #add a second line to find out what happens after Traceback line
                                #which shows an empty array (run it and look at the end!)
        continue
    print(wds[2])
    
    #4:29:01 Back to dritte.py for Ch 8 Dictionaries
    
    