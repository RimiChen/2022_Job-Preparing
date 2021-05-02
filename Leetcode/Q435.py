from typing import List

intervals = []
# intervals.append([1,2])
# intervals.append([2,3])
# intervals.append([3,4])
# intervals.append([1,3])
# intervals.append([1,2])
# intervals.append([1,2])
# intervals.append([1,2])
# intervals.append([1,2])
intervals.append([1,100])
intervals.append([11,22])
intervals.append([1,11])
intervals.append([2,12])
# intervals.append([1,3])
# intervals.append([8,10])
# intervals.append([2,6])
# intervals.append([15,18])


# [1,2],[2,3],[3,4],[1,3]
# intervals = [[1,3],[2,6],[8,10],[15,18]]

class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = self.first)
        
        result = []
        starti, endi = intervals[0]
        ans_count = 0
        for i in range(1, len(intervals)):
            startn, endn = intervals[i]
            # if endi < startn:
            #     result.append((starti, endi))
            #     starti, endi = startn, endn
            # elif endi < endn:
            #     endi = endn
            
            if startn < endi:
                ans_count = ans_count +1
                if endn > endi:
                    result.append((startn, endn))
                else:
                    result.append((starti, endi))
                    starti, endi = startn, endn
                    
            elif endi <= startn:
                # no overlap
                # result.append((starti, endi))
                starti, endi = startn, endn



        return ans_count
    
    def first(self, interval):
        return interval[0]
    
    


if __name__ == "__main__":

    obj = Solution()
    ans = obj.eraseOverlapIntervals(intervals)


    print(ans)



        