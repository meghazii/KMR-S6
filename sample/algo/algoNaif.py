#/usr/bin/python3
#-*- coding utf-8 -*-


def Overlap (text):
    overlap = []
    overlap.append(-1)
    #print(len(text))
    for i in range(0,len(text)):
        overlap.append(overlap[i] + 1)
	    #print ('Overlap[%d] = %d.' % (i,overlap[i]))  
        while overlap[i + 1] > 0 and text[i] != text[overlap[i + 1] - 1]:
            overlap[i + 1] = overlap[overlap[i + 1] - 1] + 1
    return overlap
'''
def Extraction (text,longMotif):
    longText = len(text)
    result = False
    for i in range(0,(longText - longMotif) + 1):    #On teste toutes les lettres qui peuvent comporter le motif
        #print ("")
        #print ("")
        #print ("i = %d" % (i, ))
        #print ("longText = %d" % (longText, ))
        #print ("longMotif = %d" % (longMotif, ))
        motif = text[i:i+longMotif]     #On recupere le motif
        #print (motif)
        overlap = Overlap(motif)
        #print (overlap)
        message = ''
        j = i + 1
        while j < (longText - longMotif) + 1:        
            ok = True
            l = 0
            while ok and l < longMotif:                                      
                ok = (text[j + l] == motif[l])  #Si les lettres des 2 chaines a comparer sont egales
                l += 1
            #print ("L apres le while vaut: %d" % (l, ))
            #print (ok)
            if (ok):
                if (not message):
                    message = 'Le motif %s apparait aux positions %d ' % (motif, i+1)
                    #print(message)
                message += ", %d" % (j+1, )
                l -= 1 
            #print ("L = %d" % (l, ))
            j += l - overlap[l] + 1
        if (message):
             print (message + ".")
             result = True
    return result
'''


def completeExtraction (text):
    i = len(text) - 1
    while i > 0:
        #print ("i = %d" % (i, ))
        if (naiveExtraction(text,i)):
             return i
        i -= 1
    return 0        

def naiveExtraction(text , longMotif):
    result = False
    for i in range(0,(len(text) - longMotif) + 1):    #Toutes les lettres pouvant posséder le motif
        #print ("i = %d" % (i, ))
        message = ''
        motif = text[i:i+longMotif]
        for j in range(i+1,(len(text) - longMotif) + 1):
            #print (j)
            ok = True
            l = 0
            while ok and l < longMotif:
                ok = (motif[l] == text[j + l])
                l += 1
            if (ok):
                message = "Le motif: %s apparait aux positions %d " % (motif,i + 1)
                message += ", %d " % (j + 1, )
        if (message):
            print (message + ".")
            result = True
    return result
        






if __name__ == '__main__':
    chaine = 'AABAAAABAA'
    teste = Overlap(chaine)
    #print (len(teste))
    completeExtraction(chaine)
    #print (Overlap("COCO"))
    #Extraction(chaine,5)
    #naiveExtraction(chaine,5)    
