class Solution:

    def encode(self, strs: List[str]) -> str:
        pieces = []

        for s in strs:
            num_chars = len(s)
            pieces.append(str(num_chars))
            pieces.append("#")
            pieces.append(s)
        
        encoded_string = "".join(pieces)
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0

        while i < len(s):
            # position of the "#"
            j = s.find("#", i) 
            # the characters between i and the "#"
            length = int(s[i:j])

            decoded_strs.append(s[j+1:j+length+1])
            i = j + length + 1

        return decoded_strs
