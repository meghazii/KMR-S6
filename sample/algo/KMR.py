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

def kmr(chaine,a,b):
    e = a+b
    n = numbOfChar(chaine)
    vector = findVector(chaine)

    pilesP = remplirP(vector,n)
    pilesQ = remplirQ(pilesP,vector,n,b)
    classes = findClasses(pilesQ,vector)
    nbClass = countClasses(classes,vector)

    print('e = %d' % e)
    print('a = %d' % a)
    print('b = %d' % b)
	
	sousMotif = ''
	for i in range(classes[0],classes[0]+b):
		sousMotif += chaine[i]
	print('Sous motif maximum : %s' %sousMotif)
    print(' ')

    if(nbClass == 1):
        return classes
    else:
        nextChaine = ''

        for i in range(0,len(chaine)):
            if(classes.count(i) >= 1):
                nextChaine += chaine[i]
            else:
                nextChaine += '-'
                
        if(nbClass == 0):
            x = a
            y = b/2
            return kmr(chaine,x,y)
        elif(nbClass > 1):
            x = a+a
            y = b+b
            return kmr(nextChaine,x,y)
        
    
if __name__ == '__main__':
    chaine = 'ROUDOUDOU'
    result = kmr(chaine,1,1)
    msg = 'Sous motif maximum trouvé aux positions : '
    for char in result:
        msg += '%d' %char
        
        
