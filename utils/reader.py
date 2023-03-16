def read_file():
    with open("/home/asim/Desktop/ISDP/Sir Hammad/project_weather_task/files/f1.csv") as f:
        contents = f.read()

        rows = []
        for row in contents.split("\n")[1:-1]:
            rows.append(row)
        # print(rows)

    return rows










