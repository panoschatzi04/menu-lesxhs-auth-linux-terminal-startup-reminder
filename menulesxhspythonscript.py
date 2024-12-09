import pandas as pd
import datetime

# Read the Excel file from the specified path
schedule_df = pd.read_excel("add path to python script.xlsx")

def time_to_datetime(time_obj):
    if isinstance(time_obj, datetime.time):
        today_date = datetime.datetime.today().date()
        return datetime.datetime.combine(today_date, time_obj)
    else:
        return None

current_day = datetime.datetime.now().strftime('%A')  # e.g., "Monday"
current_time = datetime.datetime.now()

current_activity = None
next_activity = None
time_until_next = None

for index, row in schedule_df.iterrows():
    if row['Day'] == current_day:
        start_time = time_to_datetime(row['Start Time'])
        end_time = time_to_datetime(row['End Time'])

        if start_time <= current_time <= end_time:
            current_activity = row['Activity']
            break
        elif current_time < start_time:
            if not next_activity or start_time < time_until_next:
                next_activity = row['Activity']
                time_until_next = start_time

if current_activity:
    print(f"Παλικάρι, η λέσχη έχει {current_day}: {current_activity}")
else:
    if next_activity:
        time_remaining = time_until_next - current_time
        hours, remainder = divmod(time_remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"Έχει ξανά μάσα: {next_activity} σε {hours} ώρες και {minutes} λεπτά")
    else:
        print(f"Δεν θα φάμε μέχρι {current_day} στις {current_time.strftime('%I:%M %p')}.")
