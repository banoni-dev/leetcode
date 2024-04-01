

def isPalindrome(x: int) -> bool:
    for i in range(len(str(x)) // 2):        
        if str(x)[i] != str(x)[-i - 1]:
            return False
    return True

print(isPalindrome(-121))
