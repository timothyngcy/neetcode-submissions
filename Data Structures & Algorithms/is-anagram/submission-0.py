class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_dict = {}

        for char in s:
            current_cnt = chars_dict.get(char, 0)
            chars_dict[char] = current_cnt + 1
        
        for char in t:
            current_cnt = chars_dict.get(char, 0)

            if current_cnt == 0:
                return False
            else:
                current_cnt = chars_dict.get(char, 0)
                chars_dict[char] = current_cnt - 1
        
        for value in chars_dict.values():
            if value != 0:
                return False

        return True
