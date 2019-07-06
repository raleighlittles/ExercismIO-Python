# # The naive recursive solution.
# def maximum_value(maximum_weight : int, items: list) -> int:
#     if (maximum_weight == 0) or (len(items) == 0):
#         return 0 # Trivial base case
#
#     # If the weight of the last item in the list is greater than the capacity
#     # As in, the last item wouldn't fit
#     elif items[-1]['weight'] > maximum_weight:
#         # Solve the problem as though that item wasn't there
#         return maximum_value(maximum_weight, items[:-1])
#
#     else:
#         # It is now possible that the last item in the list is part of your solution.
#         # To build the solution, choose the greater of the following two:
#         # The value of your 'knapsack' if you didn't add the item
#         # The value of your 'knapsack' if you had added it
#
#         # Not adding it to your knapsack is basically the same as the previous case (the `elif`)
#         value_without_item =  maximum_value(maximum_weight, items[:-1])
#
#         # If you do choose to add the item, you have to do two things:
#         # 1) Take the item out of the list of possible items. In this variation (the 0-1 case), you can't
#         # take the same item twice.
#         # 2) Once the item is in your knapsack, the remaining capacity of your knapsack decreases to account
#         # for the weight of the item.
#         last_item = items.pop()
#         value_with_item = last_item['value'] + maximum_value(maximum_weight - last_item['weight'], items)
#         return max(value_with_item, value_without_item)

# The dynamic programming solution, using the commont tabular method.
def maximum_value(maximum_weight : int, items : list):
    if len(items) == 0: return 0 # Handle the trivial case quickly

    # Pre-populate a 2d array representing the values of the knapsack for given weight limits and number of items.
    V : list = [[0] * (maximum_weight+1) for i in range(0, len(items)+1)]

    # Remember that Python ranges aren't end-inclusive
    for weight_limit in range(0, maximum_weight+1):
        for item_index in range(0, len(items)+1):
            # Minus 1 to account for 0-indexing in array
            current_item_value = items[item_index - 1]['value']
            current_item_weight = items[item_index - 1]['weight']

            # Fairly obvious: if the weight limit of the knapsack is 0, it is impossible for the sack to have
            # any value. Similarly, if there are no items in the knapsack, it has no value.
            if weight_limit == 0 or item_index == 0:
                V[item_index][weight_limit] = 0

            # If the current item can fit in the knapsack..
            elif (current_item_weight <= weight_limit):
                # Compare what the value would be if it was added to the knapsack.
                value_if_item_was_added = V[item_index - 1][weight_limit - current_item_weight] + current_item_value
                # Against what the value was if it wasn't added.
                value_if_item_wasnt_added = V[item_index -1][weight_limit]
                # The larger of those two is the best possible value of the knapsack for this weight limit
                # and number of items.
                V[item_index][weight_limit] = max(value_if_item_wasnt_added, value_if_item_was_added)
            else:
                # Here, the item doesn't fit in the capacity of the knapsack -- so the value of the knapsack
                # at this point is whatever the value would be if it wasn't there.
                V[item_index][weight_limit] = V[item_index -1][weight_limit]

    return V[-1][-1]

