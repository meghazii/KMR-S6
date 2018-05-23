#/usr/bin/python3
#-*- coding utf-8 -*-

import time
import os
import sys

class AlgoNaif:


    def __init__(self,chaine):
        self.chaine = chaine

    def getChaine(self):
        return self.chaine

    def setChaine(self, chaine):
        self.chaine = chaine

    def getMotif(self):
        return self.motif

    def setMotif(self,motif):
        self.motif = motif

    def getFirstIte(self):
        return self.firstIte

    def setFirstIte(self,i):
        self.firstIte = i

    def getSecIte(self):
        return self.secIte

    def setSecIte(self,j):
        self.secIte = j

    def getCondi(self):
        return self.condi

    def setCondi(self,condition):
        self.condi = condition

    def getThirdIte(self):
        return self.thirdIte

    def setThirdIte(self,l):
        self.thirdIte = l

    def getResult(self):
        return self.result

    def setResult(self,result):
        self.result = result
    

    def completeDetailedExtraction (self, text):    #Extraction du ou des plus grands motifs de la chaine text en version détaillé
        i = len(text) - 1
        print ("Pour la chaine %s voici le(s) plus long(s) motif(s) trouvé(s)" % (text,))
        while i > 0:
            if (self.naiveDetailedExtraction(text,i)):
                return i
            i -= 1
        return 0        

    def completeExtraction (self, text):    #Extraction du ou des plus grands motifs de la chaine text
        i = len(text) - 1
        print ("Pour la chaine %s voici le(s) plus long(s) motif(s) trouvé(s)" % (text,))
        while i > 0:
            #print ("i = %d" % (i, ))
            if (self.naiveExtraction(text,i)):
                return i
            i -= 1
        return 0


    def naiveExtraction(self, text , longMotif):    #Methode representant l'algo naif d'extraction de motif
        result = False
        for i in range(0,(len(text) - longMotif) + 1):    #Toutes les lettres pouvant posséder le motif
            #print ("i = %d" % (i, ))
            message = ''
            motif = text[i:i+longMotif]
            for j in range(i+1,(len(text) - longMotif) + 1):
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
        

    def naiveDetailedExtraction(self,text,longMotif):       #Methode pas a pas de l'algo naif avec text representant la chaine a analyser et longMotif la longueur du motif
        self.setChaine(text)    #Creation objet
        self.setResult(False)     #Passage de resultat a faux
        for i in range(0,(len(text) - longMotif) + 1):    #Toutes les lettres pouvant posseder le motif

            self.setFirstIte(i)     #Passe en attribut le premier iterateur
            motif = self.createMotif(longMotif)
            message = ''
           
            for j in range(self.getFirstIte()+1,(len(text) - longMotif) + 1):        #Comparaison avec les lettres se trouvant apres i
                self.setSecIte(j)         #Passe en attribut le deuxieme iterateur
                self.prepareMotif(longMotif)
                
                self.checkMotif(longMotif,motif)
            
                message = self.motifFound(message)
            self.editMess(message)
        return self.getResult()

    def createMotif(self, longMotif):    #Renvoie un motif: changement sur motif
        text = self.getChaine()
        motif = text[self.getFirstIte():self.getFirstIte()+longMotif]   #Creation du motif
        self.setMotif(motif)        #Passe en attribut le motif
        return self.getMotif()

    def prepareMotif(self,longM):   #Prepare les motifs a etre comparer: changements sur condi et thirdIte
        longMotif = longM
        ok = True
        self.setCondi(ok)         #Condition passe en attribut
        l = 0
        self.setThirdIte(l)       #Passe en attribut le 3eme iterateur

    def checkMotif(self,longMotif,motifAAnalyser):      #compare les 2 motifs: changements:condi et l 
        l = self.getThirdIte()
        longM = longMotif
        motif = motifAAnalyser
        while self.getCondi() == True and self.getThirdIte() < longM:   #Tant que les 2 chaines sont pareils et qu'on respecte la longueur du motif
            text = self.getChaine()
            ok = (motif[self.getThirdIte()] == text[self.getSecIte() + self.getThirdIte()])   #Si les 2 chaines ont le meme caractere a leur position L                    
            self.setCondi(ok)
            l += 1
            self.setThirdIte(l)
                           
                
    def editMess(self,mess):    #Modifie le message a renvoyer s'il n'est pas vide: changement result
        if (mess):
            print(mess + ".")
            self.setResult(True)

    def motifFound(self,message):   #message prend positions du motif trouvé: modifie message et le renvoie
        mess = message 
        if(self.getCondi()):
            mess = "Le motif: %s apparait aux positions %d " % (self.getMotif(),self.getFirstIte() + 1)
            mess += ", %d " % (self.getSecIte() + 1, )
        return mess

if __name__ == '__main__':
    
    text = AlgoNaif("ROUDOUDOU")
    chaine = text.getChaine()
    """
    text.naiveExtraction(chaine,5)
    text.naiveDetailedExtraction(chaine,5)
    """
    text.completeDetailedExtraction(chaine)
    
    text = AlgoNaif("AAABAAABAAABBAAABAAA")
    chaine = text.getChaine()
    #text.naiveExtraction(chaine,2)
    #text.naiveDetailedExtraction(chaine,3)
    text.completeDetailedExtraction(chaine)
    
    #chemin = "C:/Users/Joss/Documents/L3informatique/AlgoDeTexte/test.txt"
    chemin = ""
    if(len(sys.argv) > 1):
        chemin = sys.argv[1]
    
    if(len(chemin) >= 5):
        fichier = open(chemin,'r+')
        texte = AlgoNaif(fichier.read())
        chaine2 = texte.getChaine()
        text.completeDetailedExtraction(chaine2)