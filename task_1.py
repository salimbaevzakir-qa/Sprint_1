
time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

time_values = time_string.split(',')

total_minutes = 0

for value in time_values:
    parts = value.strip().split()
    
    for part in parts:
        if "h" in part:  # часы → минуты
            total_minutes += int(part.replace("h", "")) * 60
        elif "m" in part:  # минуты
            total_minutes += int(part.replace("m", ""))
        elif "s" in part:  # секунды → минуты
            total_minutes += int(part.replace("s", "")) // 60

print("Общее количество минут:", total_minutes)
