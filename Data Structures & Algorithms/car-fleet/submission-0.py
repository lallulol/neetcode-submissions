class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars = sorted(cars,key=lambda x: x[0], reverse=True)
        arrival_times = []
        stack = []
        stopper = 0
        for i in range(len(cars)):
            position, speed = cars[i]
            time = (target - position) / speed
            arrival_times.append(time)
        for i in arrival_times:
            if i > stopper:
                stopper = i
                stack.append(i) 
            else:
                continue
        return len(stack)

