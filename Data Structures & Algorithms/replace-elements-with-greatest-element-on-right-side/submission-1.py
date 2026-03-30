class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
            remaining_array = arr[i+1:len(arr)]
            if len(remaining_array) == 0:
                break
            else:
                arr[i] = max(remaining_array)
        return arr
        