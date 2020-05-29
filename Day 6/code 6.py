def canbuildword(s, isoriginalword, mp): 
  
    if s in mp and mp[s] == 0: 
        return False
  
    if s in mp and mp[s] == 1 and isoriginalword == 0: 
        return True
  
    for i in range(1, len(s)): 
        left = s[:i] 
        right = s[i:] 

        if left in mp and mp[left] == 1 and canbuildword(right, 0, mp): 
            return True
  
 
    mp[s] = 0
    return False

def printlongestword(listofwords): 
  

    mp = dict() 
    for i in listofwords: 
        mp[i] = 1
  

    listofwords.sort(key=lambda x: len(x), reverse=True) 

    for i in listofwords: 
  

        if canbuildword(i, 1, mp): 
            return i 
  
    return "-1"

if __name__ == "__main__": 
    listofwords = ["geeks", "for", "geeksfor", 
                "geeksforgeeks"] 
  
    print(printlongestword(listofwords))