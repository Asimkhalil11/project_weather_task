from utils.reader import read_file
from datetime import datetime

file2_content = read_file("/home/asim/Desktop/ISDP/Sir Hammad/project_weather_task/files/f2.csv")

for row in file2_content:
    event_date = row.split(",")[1]
    event = row.split(",")[22]
    if event == "Thunderstorm":
        date_object = datetime.strptime(event_date, "%Y-%m-%d")
        week_day = date_object.strftime("%A")
        print(f"{event} {week_day}")

