from utils.reader import weather_read_file

file2_content = weather_read_file("/home/asim/Desktop/ISDP/Sir Hammad/project_weather_task/files/f2.csv")

for row in file2_content:
    date_string = row.split(",")[1]
    event = row.split(",")[-2]

    if event in ["Rain", "Snow", "Rain-Snow"]:
        print(f"Date {date_string} in {event}")
