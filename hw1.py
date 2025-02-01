import heapq

def min_connection_cost_with_order(cables):
    heapq.heapify(cables)
    total_cost = 0
    merge_order = []

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second
        total_cost += cost

        merge_order.append((first, second, cost))
        heapq.heappush(cables, cost)

    return total_cost, merge_order

cables = [4, 3, 2, 6]
total_cost, merge_order = min_connection_cost_with_order(cables)

print("Total cost:", total_cost)
print("Order:")
for step, (a, b, cost) in enumerate(merge_order, 1):
    print(f"  {step}) {a} + {b} → {cost}")
