def get_file_content(file_path):
    rows_value = []

    with open(file_path) as file_read:
        file_content = file_read.read()

        for row_value in file_content.split("\n")[1:-1]:
            rows_value.append(row_value)

    return rows_value
