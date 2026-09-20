class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        systeme = [(p, v) for p, v in zip(position, speed)]
        systeme.sort(key=lambda x: x[0], reverse=True)

        temps = [(target - p) / v for p, v in systeme]

        fleets = 0
        slowest_time = 0 

        for t in temps:
            if t > slowest_time:  
                fleets += 1
                slowest_time = t  

        return fleets
