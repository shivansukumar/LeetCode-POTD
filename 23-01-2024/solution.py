class Solution:
    def maxLength(self, arr):
        ansList = [""]
        ans = 0

        for string in arr:
            if not self.uniqueCharacterString(string):
                continue

            currStr = []

            for candidate in ansList:
                temp = candidate + string
                if self.uniqueCharacterString(temp):
                    currStr.append(temp)
                    ans = max(ans, len(temp))

            ansList.extend(currStr)

        return ans

    def uniqueCharacterString(self, string):
        if len(string) > 26:
            return False
        freq = [0] * 26

        for ch in string:
            freq[ord(ch) - ord('a')] += 1
            if freq[ord(ch) - ord('a')] > 1:
                return False

        return True