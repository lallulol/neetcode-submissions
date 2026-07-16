class Solution:
    def isPalindrome(self, s: str) -> bool:
        pallindrome_list = []
        for i in s:
            if i.isalnum():
                pallindrome_list.append(i.lower())

        if pallindrome_list == pallindrome_list[::-1]:
            return True
        else:
            return False