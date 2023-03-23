from utils.reader import read_file

file2_content = read_file("/home/asim/Desktop/ISDP/Sir Hammad/project_weather_task/files/f2.csv")

for row in file2_content:
    event_date = row.split(",")[1]
    event = row.split(",")[-2]

    if event in ["Rain", "Snow", "Rain-Snow"]:
        print(f"Date {event_date} in {event}")
