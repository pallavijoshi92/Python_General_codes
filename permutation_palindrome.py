#Program to find if a given string(with or without spaces) is a permutation of a palindrome
from collections import defaultdict

def isValidPermutationPalindrome(given):
    d = defaultdict(int)
    given=given.split()
    given="".join(given)
    for k in given:
         d[k] += 1
    print d.items()
    count=0
    for k,v in d.items():
        if v%2!=0:
            count+=1
        if count > 1:
            return False
    return True

if __name__=="__main__":
    #given="tacollltanmco"
    given=raw_input("Enter string:")
    print isValidPermutationPalindrome(given)

