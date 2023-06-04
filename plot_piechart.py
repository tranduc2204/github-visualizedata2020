# 2 câu hỏi câu 1: độ tuổi các bạn thi năm nay là bao nhiu. câu thứ 2: bao nhiu bạn 17 18 19 20 ... câu 3: điểm trung bình của các bạn thi đúng tuổi có lớn hơn điểm của các bạn khác hay k
# điểm trung bình của các bạn thi 0 môn 1 môn 2 môn 3 môn 4 môn
with open ("clean_data.csv", encoding= "utf8") as file:
    data = file.read().split("\n")# biến đổi những thành phần thành mỗi dòng
    
header = data [0]
students =  data[1:]

#remove last student (empty student)
students.pop()


total_students = len (students)

header = header.split(",")
subjects = header[5:]


for i in range (len(students)):
    students[i] = students [i].split(",")

num_of_exam_taken = [0,0,0,0,0,0,0,0,0,0,0,0] # có th không thi môn nào tới thi đủ 11 môn thì 12 trường hợp
average = [0,0,0,0,0,0,0,0,0,0,0,0] # điểm trung bình của các bạn thi 0 môn 1 môn ....

print (len(num_of_exam_taken))

for s in students:
    count = 0
    total = 0
    for i in range (11):
        if s[i+5] != "-1":
            total += float(s[i+5])
            count += 1
    # if count == 1:
    #     print (s)
    
    num_of_exam_taken[count] += 1
    average[count] += total/count

for i in range (12):
    if num_of_exam_taken[i] != 0:
        average[i] = round (average[i] / num_of_exam_taken[i],2)

print (average)


import matplotlib.pyplot as plt
import numpy as np

x = np.arange(12)
y = np.arange(12)

figure, axis = plt.subplots()
plt.bar (x, average)

axis.set_ylim(0,10)  

plt.xticks(x,y)

axis.set_ylabel("Điểm trung bình")

rects = axis.patches


label = average
for rect, label in zip(rects, label):
    height =  rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height, label, ha ="center", va="bottom")


plt.ylabel("Percentage")
plt.title("Số học sinh không đi thi hoặc không đăng kí thi")
plt.show()
# print (num_of_exam_taken)
# print (len(students))

# import matplotlib.pyplot as plt

# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = "0 môn","1 môn","2 môn","3 môn","4 môn","5 môn","6 môn","7 môn","8 môn","9 môn","10 môn","11 môn"
# sizes = [0, 80, 122, 2598, 4334, 318, 2730, 64261, 0, 0, 0, 1]
# # explode = (0, 0.1, 0, 0,0,0,0,0,0,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes,  labels=labels, autopct='%1.1f%%', startangle=90)#startangle để góc bắt đầu là góc 90
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# plt.show()

