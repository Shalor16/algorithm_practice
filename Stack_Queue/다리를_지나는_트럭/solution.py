from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_on_brg = deque([])                # store (truck weight, the time when truck pass out the bridge)
    truck_weights = deque(truck_weights)    # change into Deque
    len_wait = len(truck_weights)
    truck_weights_idx = 0
    passed_truck = deque([])                # store passed truck info
    
    
    while 1:
        answer += 1 # one second later
        # not empty truck on bridge and time to pass the bridge pop out truck from queue
        if len(truck_on_brg) and (truck_on_brg[0][1] == answer):
            passed_truck.append(truck_on_brg.popleft())
            
            if len(passed_truck) == len_wait:
                return answer
        # put new truck to bridge with weight limit
        if len(truck_weights) and ((sum([i[0] for i in truck_on_brg]) + truck_weights[0]) <= weight):
            truck_on_brg.append((truck_weights.popleft(), answer + bridge_length))
    
    return answer