import time

def numbOfChar(chaine):
    print('chaine  : %s ' % chaine)    
    result = 0
    for i in range(0,len(chaine)):
        if(chaine[i] != '-'):
            if(chaine.find(chaine[i],0,i) == -1):
                result += 1    
    return result


def findVector(chaine):
    result = []
    compteur = 0
    for i in range(0,len(chaine)):
        if(chaine[i] != '-'):
            dejaVu = chaine.find(chaine[i],0,i)
            if(dejaVu == -1):
                result.append(compteur)
                compteur += 1
            else:
                result.append(result[dejaVu])
        else:
            result.append(-1)
    return result


def remplirP(vector,n):
    result = []
    for i in range(0,n):
        result.append([])
    for j in range(0,len(vector)):
        if(vector[j] != -1):
            result[vector[j]].append(j)
    return result


def remplirQ(P,vector,n,b):
    print('vector = %s' %vector)
    result = []
    for i in range(0,n):
        result.append([])
    for i in range(0,len(P)):
        for j in range(0,len(P[i])):
            if(P[i][j] + b < len(vector)):
                if(vector[ P[i][j] + b] != -1):
                    result[vector[ P[i][j] + b]].append(P[i][j])
    return result


def findClasses(Q,vector):
    qClasses = []
    result = []
    dejaVu = []

    for i in range(0,len(Q)):
        qClasses.append([])

    for i in range(0,len(Q)):
        for j in range(0,len(Q[i])):
            qClasses[i].append(vector[Q[i][j]])
    print('qClasses = %s' %qClasses)
    
    for i in range(0,len(Q)):
        for j in range(0,len(Q[i])):
            if(qClasses[i].count(qClasses[i][j]) > 1):
                result.append(Q[i][j])
    return result

def countClasses(classes,vector):
    result = 0
    dejaVu = []
    for i in range(0,len(classes)):
        if(vector[classes[i]] not in dejaVu):
            dejaVu.append(vector[classes[i]])
            result += 1
    return result

def kmr(chaine,saveChaine,a,b):
    e = a+b
    n = numbOfChar(chaine)
    vector = findVector(chaine)

    pilesP = remplirP(vector,n)
    pilesQ = remplirQ(pilesP,vector,n,b)
    classes = findClasses(pilesQ,vector)
    nbClass = countClasses(classes,vector)

    nbCstr = 'e%d' %e + ' = %d' %nbClass
    print(nbCstr)
    print('a = %d' % a)
    print('b = %d' % b)
    print('P = %s' %pilesP)
    print('Q = %s' %pilesQ)
    print('classes = %s' %classes)

    print(' ')

    nextChaine = ''
    for i in range(0,len(chaine)):
        if(classes.count(i) >= 1):
            nextChaine += chaine[i]
        else:
            nextChaine += '-'
 
    if(a == 1):
        if(b == 1):
            if(nbClass == 0):
                raise Exception('noRep')
            else:
                x = a+a
                y = b+b
            return(kmr(nextChaine,chaine,x,y))
    elif(a > 1):
        if(b == 1):
            if(nbClass >= 1):
                return classes
        elif(b > 1):
            if(nbClass == 0):
                x = a
                y = b/2
                return(kmr(nextChaine,saveChaine,x,int(y)))
            if(nbClass == 1):
                x = a
                y = b/2
                return(kmr(saveChaine,saveChaine,x,int(y)))
            else:
                x = a+a
                y = b+b
                return(kmr(nextChaine,chaine,x,y))
        
            

        
    
if __name__ == '__main__':
    chaine = 'ACTCAATGATCGGATA'
    if(chaine.find('-') != -1):
        print("Problème syntaxique, prière de ne pas mettre de '-' dans la chaine à analyser")
    else:
        try:
            result = kmr(chaine,chaine,1,1)
            print(result)
            msg = 'Sous motif maximum trouvé aux positions : '
            for char in result:
                msg += '%d, ' %char
            print(msg)
        except Exception as error:
            print("Il n'y a aucun motif qui se répète dans cette séquence")
    
        
