def weather_read_file(path):
    file_rows = []

    with open(path) as file_read:
        file_content = file_read.read()
        for row in file_content.split("\n")[1:-1]:
            file_rows.append(row)

    return file_rows
