class Solution:
    def findID(self, user_IDs, id):
        left, right = 0, len(user_IDs) - 1

        while left <= right:
            mid = (left + right) // 2
            if user_IDs[mid] == id:
                return mid
            elif user_IDs[mid] < id:
                left = mid + 1
            else:
                right = mid - 1
        return -1
            