class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars = sorted(cars, key=lambda x:x[0], reverse=True)
        arrival_times = []
        stopper = -1
        stack = []
        for i in range(len(cars)):
            pos, spd = cars[i]
            arrival_time = (target-pos)/spd
            arrival_times.append(arrival_time)
        for i in arrival_times:
            if i > stopper:
                stopper = i
                stack.append(i)
            else:
                continue
        return len(stack)