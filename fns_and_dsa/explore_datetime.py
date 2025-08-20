import datetime

now = datetime.datetime.now()
print("Current Date and Time:", now)

today = datetime.date.today()
print("Today's Date:", today)

formatted_date = now.strftime("%A, %B %d, %Y %H:%M:%S")
print("Formatted Date:", formatted_date)

# Add 7 days
next_week = today + datetime.timedelta(days=7)
print("Date after 7 days:", next_week)
