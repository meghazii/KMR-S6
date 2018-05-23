#/usr/bin/python3
#-*- coding utf-8 -*-
class AlgoNaif:


    def __init__(self,chaine):
        self.chaine = chaine

    def getChaine(self):
        return self.chaine
    
    def Overlap(self, text):
        overlap = []
        overlap.append(-1)
        #print(len(text))
        for i in range(0,len(text)):
            overlap.append(overlap[i] + 1)
	    #print ('Overlap[%d] = %d.' % (i,overlap[i]))  
            while overlap[i + 1] > 0 and text[i] != text[overlap[i + 1] - 1]:
                overlap[i + 1] = overlap[overlap[i + 1] - 1] + 1
        return overlap


    def completeExtraction (self, text):
        i = len(text) - 1
        while i > 0:
            #print ("i = %d" % (i, ))
            if (self.naiveExtraction(text,i)):
                return i
            i -= 1
        return 0        

    def naiveExtraction(self, text , longMotif):
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
    text = AlgoNaif("AABAAAABAA")
    #chaine = 'AABAAAABAA'
    chaine = text.getChaine()
    teste = text.Overlap(chaine)
    text.completeExtraction(chaine)
    #print (Overlap("COCO"))
    #Extraction(chaine,5)
    #naiveExtraction(chaine,5)

        
