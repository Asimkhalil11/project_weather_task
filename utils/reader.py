def read_file(path):
    rows = []

    with open(path) as file_read:
        content = file_read.read()
        for row in content.split("\n")[1:-1]:
            rows.append(row)

    return rows



