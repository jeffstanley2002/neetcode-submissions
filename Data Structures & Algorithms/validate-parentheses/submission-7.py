class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': ')', '[': ']', '{': '}'}
        st = []

        for ch in s:
            if ch in d:
                st.append(ch)
            else:
                if not st or d[st.pop()] != ch:
                    return False

        return not st