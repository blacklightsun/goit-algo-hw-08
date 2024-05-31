import heapq

cables_list = [5, 6, 2, 1, 8, 12, 14, 7, 10,]

# for i in cables_list:
heapq.heapify(cables_list)
print(f'\nStart heap: {cables_list}')
step_list = []
step_counter = 0

while len(cables_list) > 1:
    step_counter += 1
    cable1 = heapq.heappop(cables_list)
    cable2 = heapq.heappop(cables_list)
    combined_cable = cable1 + cable2
    heapq.heappush(cables_list, combined_cable)
    heapq.heapify(cables_list)
    step_list.append((cable1, cable2,))
    print(f'Step {step_counter:>2d}: cable1={cable1:>3d}, cable2={cable2:>3d}, combined_cable={combined_cable:>4d}, heap={cables_list}')

print(f'The order of the steps: {step_list}\n')