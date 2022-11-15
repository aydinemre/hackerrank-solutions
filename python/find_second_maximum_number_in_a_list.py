"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.
"""

"""
Sorting vs Find Max Value:

- Sorting Complexity: O(Nlogn):https://stackoverflow.com/q/14434490/8289026
- Find max value of list complexity O(N):https://stackoverflow.com/q/5454030/8289026
"""
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    max_val = max(arr)
    while max(arr) == max_val:
        arr.remove(max_val)
    print(max(arr))
