from utils.contants import MapperIndexF1
from utils.reader import get_file_content

file_content = get_file_content("/home/asim/Desktop/ISDP/Sir Hammad/project_weather_task/files/f1.csv")

for row_content in file_content:
    date_column = row_content.split(",")[MapperIndexF1.DATE]
    max_temperature = row_content.split(",")[MapperIndexF1.MAX_TEMPERATURE]
    min_temperature = row_content.split(",")[MapperIndexF1.MIN_TEMPERATURE]

    max_min_difference = int(max_temperature) - int(min_temperature)
    print(f"{date_column} Maximum & Minimum Difference {max_min_difference}")
