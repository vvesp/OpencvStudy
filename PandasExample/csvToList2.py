import csv
students = []
for num in range(1,4):
    filename = "class{}".format(num) #class1 ~ 4.CSV 파일 로드
    file = open(filename,"r")
    csvfile = csv.reader(file)
    for item in csvfile:
        sum = 0
        for score in item[1:]:
            sum += int(score)
        avg = sum / (len(item) - 1)
        item.append(avg)
        students.append(item)

file = open("students1.csv","w",newline="")
csvfile = csv.writer(file)
for student in students:
    csvfile.writerow(students)
file.close()