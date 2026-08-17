class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = [0] * 1000
        length = 0
        n = len(operations)
        for i in operations :
            if i == "+" :
                score[length] = score[length-1] + score[length-2]
                length = length + 1         
            elif i == "C" :
                score[length-1] = [0]
                length = length - 1
            elif i == "D" :
                score[length] = 2 * score[length-1]
                length = length + 1
            else :
                score[length] = int(i)
                length = length + 1
        sum = 0
        for i in range(length) :
            sum = sum + score[i]
        return sum   