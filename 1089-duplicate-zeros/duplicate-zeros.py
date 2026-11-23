class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        i = 0
        j = 0

        # for i in range(0,len(arr)-1, 1):
        while i<len(arr)-1:
            if arr[i]==0:
                for j in range(len(arr)-1, i, -1):
                    arr[j] = arr[j-1]
                i+=1
            i+=1
        print(arr)