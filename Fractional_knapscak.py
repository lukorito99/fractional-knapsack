#Partial selection of item is allowed
#Three ways using greedy method,will use profit by weight ratio
#maximum profit by weight ratio
#maximum profit
#minimum weights

def fractional_knapsack(weights, capacity ,values):

    profit_ratio = [p/w for p,w in zip(values,weights)]
    profit_ratio.sort(reverse=True)

    optimal_value=0.0
    optimal_combo=[0] * len(weights)

    for i in profit_ratio:

        if weights[profit_ratio.index(i)] <= capacity:
            optimal_combo[profit_ratio.index(i)] = 1
            optimal_value += values[profit_ratio.index(i)]
            capacity -= weights[profit_ratio.index(i)]
        else:
            optimal_combo[profit_ratio.index(i)] = capacity/weights[profit_ratio.index(i)]
            optimal_value += values[profit_ratio.index(i)] * (capacity/weights[profit_ratio.index(i)])
            break

    print('Optimal Profit: ',optimal_value,'\nOptimal Combination: ',*optimal_combo)


weights=list()
values=list()

item_count=int(input('How many items are available?:\n'))
capacity=int(input('What is the capacity?:\n'))


for i in range(item_count):
    print('\nEnter weight for item:',i+1)
    weights.append(float(input('')))
    print('\nEnter the corresponding value for item:',i+1)
    values.append(float(input('')))


fractional_knapsack(weights, capacity ,values)
