from utils.reader import read_file_f2

file_values = read_file_f2()
# print(file_values)


for row in file_values:
    date = row.split(",")[1]
    event = row.split(",")[22]

    if event == "Rain" or event == "Snow" or event == "Rain-Snow":
        print(date,event)
        # print(event)