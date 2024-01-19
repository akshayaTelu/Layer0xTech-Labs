def longest_palindrome(s):
  """
  Finds the longest palindromic substring in a given string.

  Args:
    s: The input string.

  Returns:
    The longest palindromic substring in the input string.
  """

  n = len(s)
  dp = [[0 for _ in range(n)] for _ in range(n)]

  # Base case: All single characters are palindromes of length 1.
  for i in range(n):
    dp[i][i] = 1

  # Fill the DP table in bottom-up manner.
  for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
      if s[i] == s[j]:
        dp[i][j] = dp[i + 1][j - 1] + 2
      else:
        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

  # Find the longest palindromic substring.
  max_len = 0
  start = 0
  for i in range(n):
    for j in range(i, n):
      if dp[i][j] > max_len:
        max_len = dp[i][j]
        start = i

  return s[start:start + max_len]

# Example usage
input_str = "babad"
longest_pal = longest_palindrome(input_str)
print(f"Longest palindrome in '{input_str}': {longest_pal}")