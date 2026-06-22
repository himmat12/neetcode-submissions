class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        encoding = []
        content = []
        for each_str in strs:
            count = len(each_str)
            encoding.append(f"{count}_#_")
            content.append(each_str)
        return f"{"".join(encoding)}{"".join(content)}"


    def decode(self, s: str) -> List[str]:
        arr = s.split('_#_')
        raw_str = arr.pop()

        i, j, decoded = 0, 0, []

        for n in arr:
            j += int(n)
            decoded_str = raw_str[i:j]
            decoded.append(decoded_str)
            i = j
        return decoded
