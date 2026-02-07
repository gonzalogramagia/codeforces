total_houses, _ = map(int, input().split())
houses_tasks = list(map(int, input().split()))

time = 0
current_house = 1

for house_task in houses_tasks:
    if house_task >= current_house:
        time += house_task - current_house
    else:
        time += (total_houses - current_house) + house_task
    current_house = house_task

print(time)