# read file
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

not_take_exam = [0,0,0,0,0,0,0,0,0,0,0]


# print (students[-1])
print (len(not_take_exam))
# loop through all students
for s in students:
    # loop through all subject
    for i in range (5,16): # có 11 môn lặp qua hết là 5 tới 16 là điểm hs
        if s[i] == "-1":
            not_take_exam[i-5] += 1
# đếm xem có ai không thi môn nào không
print (not_take_exam)

not_take_exam_percentage = [0,0,0,0,0,0,0,0,0,0,0]
for i in range (0,11):
    not_take_exam_percentage[i] = round(not_take_exam[i] *100 / total_students,2) 
print (not_take_exam_percentage)
print (subjects)



# # importing library
# import matplotlib.pyplot as plt
 
# # function to add value labels
# def addlabels(x,y):
#     for i in range(len(x)):
#         plt.text(i,y[i],y[i])


import matplotlib.pyplot as plt
import numpy as np
 
figure, axis = plt.subplots()

y_pos =  np.arange(len(subjects))

plt.bar (y_pos, not_take_exam_percentage)
plt.xticks(y_pos,subjects)

axis.set_ylim(0,100)

# addlabels (subjects, not_take_exam)

rects = axis.patches
for rect, label in zip(rects, not_take_exam):
    height =  rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha ="center", va="bottom")


plt.ylabel("Percentage")
plt.title("Số học sinh không đi thi hoặc không đăng kí thi")
plt.show()



