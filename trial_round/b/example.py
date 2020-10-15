def deduplicate_alarms(alarms, period):
  deduplication = {}

  for alarm in alarms:
    remainder = alarm % period
    if deduplication.get(remainder):
      if remainder > deduplication.get(remainder):
        deduplication[remainder] = alarm
    else:
      deduplication[remainder] = alarm

  return deduplication

def find_call(period, alarms, alarm_limit):
  high = pow(10, 9) * pow(10, 9)
  low = 0

  while low <= high:
    m = (low + high) // 2
    
    if alarm_clock(m, period, alarms) < alarm_limit:
      low = m + 1
    else:
      high = m - 1
      
  if alarm_clock(m, period, alarms) == alarm_limit:
    return low
  else:
    return high + 1

def alarm_clock(moment_of_time, period, alarms):
  rings = 0
  
  for alarm in alarms:
    if alarm <= moment_of_time:
      rings += max((moment_of_time - alarm) // period, 0) + 1

  return rings

def main():

  with open('input.txt') as fp:
    alarm_count, period, alarm_limit = [int(num) for num in fp.readline().split()]
    alarms = [int(num) for num in fp.readline().split()]
    
  alarms.sort()

  deduplicated_alarms = deduplicate_alarms(alarms, period)
  alarms = list(deduplicated_alarms.values())

  found_call = find_call(period, alarms, alarm_limit)

  print(found_call)

main()