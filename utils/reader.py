def read_file(path):
    file_rows = []

    with open(path) as file_read:
        content = file_read.read()
        for row in content.split("\n")[1:-1]:
            file_rows.append(row)

    return file_rows



