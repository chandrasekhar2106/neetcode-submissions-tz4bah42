class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we wanted to ingonre all except alphanumeric
        # we wanted to convert to lower case
        left, right = 0, len(s)-1

        while left <= right:
            is_alpha_num = True
            if not s[left].isalnum():
                left += 1
                is_alpha_num = False
            if not s[right].isalnum():
                right -= 1
                is_alpha_num = False
            if is_alpha_num:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True