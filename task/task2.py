from utils.reader import read_file

files_values = read_file()

for row in files_values:
    date = row.split(",")[0]
    max_temp = row.split(",")[1]
    min_temp = row.split(",")[3]

    max_min_diff = int(max_temp) - int(min_temp)
    average = max_min_diff/2
    print(date, "Maximum & Minimum average", average)








