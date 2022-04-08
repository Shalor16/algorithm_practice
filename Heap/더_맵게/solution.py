import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # make scoville list to heap

    while 1:

        if scoville[0] < K: # if scoville[0] is lower than K, there need to be mixing process
            # if mixing is continued, one data will be storeed in scoville heap at the end. In that moment, scoville[0] is lower than K
            # that means fail to make higher than K. So stop return -1
            if len(scoville) == 1: 
                return -1
            # get minimum value and next minimum value
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a + 2 * b)
            answer += 1
        else:   # every scoville is higher or same as K. So stop then return the answer
            break
    return answer

#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges