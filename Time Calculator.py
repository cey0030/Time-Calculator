def add_time(start, duration, day=None):
  resultAmPm = "AM"
  amPm = start.split()[1]
  startMinutes = start.split()[0].split(':')[1]
  start = start.split()[0].split(':')
  duration = duration.split(':')
  start = int(start[0])
  if amPm == 'PM':
    start = start + 12
  resultHours = start + int(duration[0])
  resultMinutes = int(startMinutes) + int(duration[1])
  if resultMinutes > 60:
    resultHours = resultHours + resultMinutes // 60
    resultMinutes = resultMinutes % 60
  daysPassed = 0
  if resultHours > 24:
    daysPassed = resultHours // 24
    resultHours = resultHours % 24
  if resultHours >= 12:
    resultAmPm = "PM"
    resultHours = resultHours - 12
  if resultHours == 0:
    resultHours = resultHours + 12
  if len(str(resultMinutes)) == 1:
    resultMinutes = "0" + str(resultMinutes)
  new_time = str(resultHours) + ":" + str(resultMinutes) + " " + resultAmPm
  days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
  if day is not None: 
    dayIndex = days.index(day.lower())
    dayIndex = dayIndex + daysPassed
    if dayIndex > 6:
      dayIndex = dayIndex % 7
    new_time += ", " + days[dayIndex].capitalize()
  if daysPassed == 1:
    new_time += ' (next day)'
  if daysPassed > 1:
    new_time += " (" + str(daysPassed) + " days later)"
  return new_time