class Solution:
    def planVacation(self, miles, target):
        n = len(miles)
        min_length = n + 1
        left, sum_miles = 0, 0

        for right in range(n):
            sum_miles +=  miles[right]
            while sum_miles >= target:
                min_length = min(min_length, right - left + 1)
                sum_miles -= miles[left]
                left += 1
        return min_length if min_length <= n else 0