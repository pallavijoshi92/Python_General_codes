#program to check if a given number/string is a palindrome
import sys

def isPalindrome(given):
    given="".join(given.split())
    if len(given)==0:
        print "No string entered"
        sys.exit()       
    for i in range(len(given)//2):
        if given[i]!=given[-1-i]:
            return False
    return True 
    
if __name__=="__main__":
    given=raw_input("Enter string/number:")
    print isPalindrome(given)    
    