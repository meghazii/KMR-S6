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


def findClasses(source,chaine,Q,vector,a,b):
    result = []
    dejaVu = []
    compteur = 0

    for i in range(0,len(Q)):
        for j in range(0,len(Q[i])):
                if(source[Q[i][j]:(Q[i][j]+a+b)] not in dejaVu):      
                    result.append([])
                    dejaVu.append(source[Q[i][j]:(Q[i][j]+a+b)])
                    result[compteur].append(Q[i][j])
                    compteur += 1
                else:
                    for k in range(0,len(dejaVu)):
                        if(dejaVu[k] == source[Q[i][j]:(Q[i][j]+a+b)]):
                            result[k].append(Q[i][j])

    return result

def countClasses(classes):
    result = 0
    for i in range(0,len(classes)):
        if(len(classes[i]) > 1):
            result += 1
    return result

def reducClasses(classes):
    result = []
    for i in range(0,len(classes)):
        for j in range(0,len(classes[i])):
            if(len(classes[i]) > 1):
                result.append(classes[i][j])
    return result

def kmr(source,chaine,a,b,res):
    e = a+b
    n = numbOfChar(chaine)
    vector = findVector(chaine)

    pilesP = remplirP(vector,n)
    pilesQ = remplirQ(pilesP,vector,n,b)
    classes = findClasses(source,chaine,pilesQ,vector,a,b)
    nbClass = countClasses(classes)

    nbCstr = 'e%d' %e + ' = %d' %nbClass
    print(nbCstr)
    print('a = %d' % a)
    print('b = %d' % b)
    print('P = %s' %pilesP)
    print('Q = %s' %pilesQ)
    print('classes = %s' %classes)
    print('classes precedentes = %s' %res)

    nextChaine = ''
    reducClass = reducClasses(classes)
    print('red class = %s ' %reducClass)
    for i in range(0,len(chaine)):
        if(reducClass.count(i) >= 1):
            nextChaine += chaine[i]
        else:
            nextChaine += '-'
 
    print(' ')

    if(a == 1):
        if(b == 1):
            if(nbClass == 0):
                raise Exception('noRep')
            else:
                x = a+a
                y = b+b
            return(kmr(source,nextChaine,x,y,classes))
    elif(a > 1):
        if(b == 1):
            if(nbClass >= 1):
                return classes
            elif(nbClass == 0):
                return res
            
        elif(b > 1):
            if(nbClass == 0):
                x = a
                y = b/2
                return(kmr(source,chaine,x,int(y),res))
            elif(nbClass == 1):
                return classes
            else:
                x = a+a
                y = b+b
                return(kmr(source,nextChaine,x,y,classes))
        
            

        
    
if __name__ == '__main__':
    chaine = 'ACTGTGCTGACTGTGATCGATCGATTTAGC'
    if(chaine.find('-') != -1):
        print("Problème syntaxique, prière de ne pas mettre de '-' dans la chaine à analyser")
    else:
        result = kmr(chaine,chaine,1,1,[])
        res = reducClasses(result)
        if(not res):
            res = []
            for i in range(0,len(result)):
                res.append(result[i][0])
        msg = 'Sous motif maximum trouvé aux positions : '
        for i in range(0,len(res)):
            msg += '%d, ' %(res[i]+1)
        print(msg)        
