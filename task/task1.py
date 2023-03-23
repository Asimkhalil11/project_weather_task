from utils.reader import read_file

file1_content = read_file("/home/asim/Desktop/ISDP/Sir Hammad/project_weather_task/files/f1.csv")

for row in file1_content:
    event_date = row.split(",")[0]

    max_temp = row.split(",")[1]
    min_temp = row.split(",")[3]

    max_min_diff = int(max_temp) - int(min_temp)
    print(f"{event_date} Maximum & Minimum Diff {max_min_diff}")