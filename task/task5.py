from utils.contants import MapperIndexF2
from utils.reader import get_file_content

file_content = get_file_content("/home/asim/Desktop/ISDP/Sir Hammad/project_weather_task/files/f2.csv")

for row_content in file_content:
    date_column = row_content.split(",")[MapperIndexF2.DATE]
    event_column = row_content.split(",")[MapperIndexF2.EVENT]

    if event_column in ["Rain", "Snow", "Rain-Snow"]:
        print(f"Date {date_column} in {event_column}")
