class HighestValueCommonSubsequence:
    def maximumValue(strA, strB, charValues):
        # initialize string input
        A = len(strA) 
        B = len(strB)

        # https://www.geeksforgeeks.org/python/dynamic-programming-in-python/
        # https://high-python-ext-3-algorithms.readthedocs.io/ko/latest/chapter8.html
        # initialize dp table
        dp = [[0] * (B + 1) for _ in range(A + 1)]

        # fill dp table
        for i in range(1, A + 1):
            for j in range(1, B + 1):
                if strA[i - 1] == strB[j - 1]:
                    val = charValues.get(strA[i - 1], 0)
                    dp[i][j] = max(dp[i - 1][j - 1] + val, dp[i - 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # reconstruct the longest common subsequence
        result = []
        i, j = A, B
        while i > 0 and j > 0:
            if strA[i - 1] == strB[j - 1]:
                result.append(strA[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        # return the maximum value and the longest common subsequence
        return dp[A][B], ''.join(reversed(result))