
# Function for task1 and task2 max and min difference and average
def read_file():
    with open("/home/asim/Desktop/ISDP/Sir Hammad/project_weather_task/files/f1.csv") as f:
        contents = f.read()

        rows = []
        for row in contents.split("\n")[1:-1]:
            rows.append(row)
        # print(rows)

    return rows





# Function for task5 max anddates in which the Event "Snow", "Rain" or "Rain-Snow"
def read_file_f2():
    with open("/home/asim/Desktop/ISDP/Sir Hammad/project_weather_task/files/f2.csv") as file_read:
        contents = file_read.read()
        # print(contents)

        rows = []
        for row in contents.split("\n")[1:-1]:
            rows.append(row)
    return rows





