#------------------------------------------------------------------------------
#-----------------------Made by George Leonard 15/09/2019----------------------
#------------------------------------------------------------------------------

def addword(word, array):
    array.append(list(word))

def points(wordindex, array, compareword):
    word = array[int(wordindex)]
    pointnumber = 0
    if len(array[wordindex]) == len(compareword):
        pointnumber = pointnumber+1
        for c in word:
            if c in compareword:
                pointnumber = pointnumber+1
        return pointnumber
    else:
        for c in word:
            if c in compareword:
                pointnumber = pointnumber+1
        return pointnumber        

def unscramble(word, array):
    pointlist = []
    print(word)
  
    for i in range(len(array)):
        t = points(i, array, word)
        pointlist.append(t)
    for i in pointlist:
        
        if i == len(word)+1 and len(array[pointlist.index(i)]) == len(word):
            print("Exact match is:", array[pointlist.index(i)])
            unscrambled = array[pointlist.index(i)]
            for c in unscrambled:
                for i in (" [],''"):
                    unscrambled = str(unscrambled).replace(i, '')
            return str(unscrambled)
            break
        if max(pointlist) == 0 or max(pointlist) == 1:
            print("No similar words found. Add to your list!")
            print("")
        else:
            print(str(array[pointlist.index(i)]) + "is a close match, it has: " + str(i) + "points")

test = []
addword("oldschool-prison", test)
addword("thor", test)
test = unscramble("tohr", test)
print(test)

#https://github.com/George-Leonard/
