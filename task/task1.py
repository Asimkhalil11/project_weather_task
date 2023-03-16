from utils.reader import read_file

files_values = read_file()

for row in files_values:
    # print(row)
    date, max_temp, min_temp = row.split(",")[0:2]+ row.split(",")[3:4]
    max_min_diff = int(max_temp) - int(min_temp)

    print(date, "Maximum & Minimum Diff", max_min_diff)
