# 2 câu hỏi câu 1: độ tuổi các bạn thi năm nay là bao nhiu. câu thứ 2: bao nhiu bạn 17 18 19 20 ... câu 3: điểm trung bình của các bạn thi đúng tuổi có lớn hơn điểm của các bạn khác hay k
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
# lấy số học sinh mỗi nhóm tuổi 
num_of_student_per_age_group = [0,0,0,0,0,0,0,0,0,0,0] # 11 nhóm tuổi 
# print (len(num_of_student_per_age_group))
average_of_student_per_age_group = [0,0,0,0,0,0,0,0,0,0,0] 

for s in students:
    age = 2020 - int (s[4])
    if age >= 27:
        age = 27
    num_of_student_per_age_group[age - 17] += 1 # age -17 là age từ 17 tới 27   
    
    sum_score = 0 # tổng điểm 
    count_score = 0 # số môn thi
    for i in range (11):
        if s[i+5] != "-1":
            count_score += 1
            sum_score += float (s[i+5])


    average = sum_score / count_score
    average_of_student_per_age_group[age -17] += average
   
for i in range (len(average_of_student_per_age_group)):
    average_of_student_per_age_group[i] = round(average_of_student_per_age_group[i] / num_of_student_per_age_group[i],2)
    
for i in range (len(average_of_student_per_age_group)):
    average_of_student_per_age_group[i] = average_of_student_per_age_group[i] * 70000 /10


print (num_of_student_per_age_group)
print (average_of_student_per_age_group)

 
import matplotlib.pyplot as plt
import numpy as np

age_lable = [17,18,19,20,21,22,23,24,25,26,">26"]

x = np.arange(11)
y = np.arange(11)

figure, axis = plt.subplots()
plt.bar (x, num_of_student_per_age_group)
plt.plot(x, average_of_student_per_age_group, color="red", marker ="o") # donfg vex line chart
#set limit
axis.set_ylim(0,70000)

plt.xticks(x, age_lable)

axis.set_ylabel("Số học sinh")
axis.set_xlabel("Tuổi")

# taoj trucj cho line chart
axis2 = axis.twinx()
axis2.tick_params("y", colors="r")
axis2.set_ylabel("Điểm trung bình")
axis2.set_ylim(0,10)

rects = axis.patches
label = [2, 66327, 4463, 1396, 767, 384, 300, 223, 177, 109, 296]
for rect, label in zip(rects, label):
    height =  rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height +2, label, ha ="center", va="bottom")

plt.title("Điểm trung bình theo độ tuổi")
plt.show()
    
    
    
    
    
    
