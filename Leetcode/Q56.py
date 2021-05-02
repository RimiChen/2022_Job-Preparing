from typing import List

intervals = []
intervals.append([1,3])
intervals.append([8,10])
intervals.append([2,6])
intervals.append([15,18])

# intervals = [[1,3],[2,6],[8,10],[15,18]]

class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # input list
        # output list
        result = []
        # result.append([1,6])
        # result.append([8,10])
        # result.append([15,18])

        sorted_by_start = sorted(intervals, key=lambda x: x[0])


        # while interval list not empty
        # temp_end_list = []

        while len(sorted_by_start) > 0:
            # print("old ======")
            # print(sorted_by_start)

            # record the first end
            current_min_start, current_max_end = sorted_by_start[0]

            if len(sorted_by_start) > 1:
                sorted_by_start.pop(0)
            
            # print("new ======")
            # print(sorted_by_start)

            # viewed_list = []
            count = 0
            for inter in sorted_by_start:
                # print(inter)
                if inter[0] <= current_max_end:
                    # inside current interval
                    if inter[1] > current_max_end:
                        # part out the interval
                        # update the current_max_end
                        current_max_end = inter[1]

                    # else:
                    #     # all in interval
                    #     # skip this and remove from the list
                    #     print("do nothing and just skip")

                    # viewed_list.append(inter)
                    count = count + 1
                # else:
                #     print("not in the same interval")

                    # substract viewed intervals
            for i in range(count):
                sorted_by_start.pop(0)
            # new_intervals = [item for item in sorted_by_start if item not in viewed_list]
            # sorted_by_start = sorted(new_intervals, key=lambda x: x[0])

                # else:

            result.append([current_min_start, current_max_end])



        # final_result = []
        # [final_result.append(x) for x in result if x not in final_result]

        # return final_result
        return result

if __name__ == "__main__":

    obj = Solution()
    ans = obj.merge(intervals)


    print(ans)



        