time = '1h 45m,360s,25m,30m 120s,2h 60s'

time_parts = time.split(',')
total_minutes = 0

for part in time_parts:
    formatted_part = part.replace(' ', ',')
    elements = formatted_part.split(',')

    for element in elements:
        if 'h' in element:
            total_minutes += int(element.replace('h', '')) * 60
        elif 'm' in element:
            total_minutes += int(element.replace('m', ''))
        elif 's' in element:
            total_minutes += int(element.replace('s', '')) // 60


print(total_minutes)
