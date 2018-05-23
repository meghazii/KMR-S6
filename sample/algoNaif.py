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

def Extraction (text, longMotif):
        longText = len(text)
        l = 0
        result = False
        for i in range(0,(longText - longMotif)):
                print ("i = %d" % (i, ))
                print ("longText = %d" % (longText, ))
                print ("longMotif = %d" % (longMotif, ))
                motif = text[i:i+longMotif]
                overlap = Overlap(motif)
                print (overlap)
                message = ''
                j = i + 1
                while j < longText - longMotif:
                        ok = True
                        for l in range(l,longMotif) if ok:                                      
                                ok = (text[j + 1] == motif[l])
                        if (ok):
                                if (not message):
                                        message = 'Le motif %s apparait aux positions %d ' % (motif, i)
                                        print(message)
                                message += ", %d" % (j, )
                                l -= 1
                        j += l - overlap[l + 1] + 1
                if (message):
                        print (message + ".")
                        result = True
        return result

def completeExtraction (text):
        i = len(text) - 1
        while i > 0:
                if (Extraction(text,i)):
                        return i
                i -= 1
        return 0        



if __name__ == '__main__':
	chaine = 'AABAABABA'
	teste = Overlap(chaine)
	#print (len(teste))
	#completeExtraction(chaine)
        print (Overlap("COCO"))

        
