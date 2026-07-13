#Q-1. Best Time to Buy And Sell Stock
def Buy_Sell(prices):
    n=len(prices)
    left=0
    right=1
    max_profit=0
    while right<n:
        if prices[left]<prices[right]:
            current_profit=prices[right]-prices[left]
            max_profit=max(current_profit,max_profit)
        else:
            left=right
        
        right+=1
    
    return max_profit


prices=[int(x) for x in input().split()]
print(Buy_Sell(prices))