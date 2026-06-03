class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        aft = start + 1
        end = len(prices)
        profit = 0
        maxProfit = -1
        print(end)
        if (end == 1):
            return 0
        profit = prices[aft] - prices[start]
        if (end == 2 and profit <= 0):
            return 0
        elif (end == 2 and profit >= 0):
            return profit
        else:
            while(start < end and aft < end):
                print("Aft:", aft, "Aft Index Value", prices[aft])
                print("Start:", start, "Start Index Value", prices[start])
                
                profit = prices[aft] - prices[start]
                print("Current Profit:", profit)
                if (maxProfit < profit):
                    maxProfit = profit
                aft += 1
                print("Max Profit:", maxProfit)
                if (aft == end):
                    start += 1 
                    aft = start + 1
            if (maxProfit <= 0):
                maxProfit = 0
            print("Final Max Profit:", maxProfit)
        return maxProfit
            
            

