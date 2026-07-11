#Q-1. Valid Palindrome
#TC-> O(n) SC->O(1)
def palindrome(word):
    n=len(word)
    left=0
    right=n-1

    while left<right:
        if word[left] != word[right]:
            return False
        left +=1
        right-=1

    return True

word=input()
print(palindrome(word))