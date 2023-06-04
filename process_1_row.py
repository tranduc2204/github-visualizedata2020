import csv
file = open("raw_data.txt", "r")

#code by teedee
datas = file.read().split("\n")

file = open ("clean_data.csv", encoding="utf8", mode= "w")

with open("clean_data.csv", encoding="utf8", mode= "w", newline ='') as file_csv:
    header = ["sbd", "tên", "dd", "mm", "yy", "toán", "ngữ văn", "khxh", "khtn","lịch sử", "địa lí", "gdcd", "sinh học", "vật lí", "hóa học", "tiếng anh"]
    writer = csv.writer(file_csv)
    writer.writerow(header)

sbd =  2000000

for data in datas:
    try:
        sbd +=1
        sbd_str = "0"+str(sbd)
        data = data.split ("\\n")

        for i in range(len(data)):
            data[i] = data[i].replace("\\r", "")
            data[i] = data[i].replace("\\t", "")
            
            
        # remove tag
        for i in range (len(data)):
            tags = []
            for j in range (len(data[i])):
                if data[i][j] == "<":
                    begin = j
                elif data[i][j] == ">":
                    end = j    
                    tags.append(data[i][begin: end+1])
                    
            for tag in tags:
                data[i] =  data[i].replace(tag, "")    

        for i in range(len(data)):
            # xóa  khoảng troiongs trước sau
            data[i] =  data[i].strip()

        # xóa dòng enter
        unempty_line = []
        for i in range(len(data)):
            if data[i] != "":
                unempty_line.append(data[i])
        data =  unempty_line


        # chọn các thông tin cần thôi
        name = data[7]
        date_of_birth = data [8]
        scores = data[9]
        print (name)
        print (date_of_birth)
        print (scores)




        # load unicode table
        chars = []
        codes = []

        file = open("unicode.txt", encoding="utf8")
        unicode_table = file.read().split("\n")

        for code in unicode_table:
            x = code.split (" ")
            chars.append(x[0])
            codes.append(x[1])



        # đặt lại tên và điểm
        for i in range (len(chars)):
            name = name.replace(codes[i], chars[i])
            scores = scores.replace(codes[i], chars[i])

        for i in range (len(name)):
            if name[i:i+2] == "&#":
                name = name[:i] + chr(int (name[i+2: i+5])) + name [i+6:]
            
        for i in range (len(scores)):
            if scores[i:i+2] == "&#":
                scores = scores[:i] + chr(int (scores[i+2: i+5])) + scores [i+6:]


        # chuyển hết về viết thường
        name = name.lower()
        scores = scores.lower()

        dob_list = date_of_birth.split("/")
        dd = int (dob_list[0])
        mm = int (dob_list[1])
        yy = int (dob_list[2])


        #process scores
        # remove
        scores = scores.replace(":", "")

        scores =  scores.replace("khxh ", "khxh   ")

        scores =  scores.replace("khtn ", "khtn   ")
        scores_list = scores.split("   ")
        print (scores_list)


        data = [sbd_str, name.title(), str(dd), str(mm), str(yy)]

        # add score to row data

        for subject in ["toán", "ngữ văn", "khxh", "khtn", "lịch sử", "địa lí", "gdcd", "sinh học", "vật lí", "hóa học", "tiếng anh"]:
            if subject in scores_list:
                #data.append(str(float(scores_list[scores_list.index(subject)+1])))
                subject_name_position =  scores_list.index (subject)
                subject_score_position = subject_name_position + 1
                subject_core =  scores_list[subject_score_position]
                data.append(str(subject_core))
            else:
                data.append("-1")

        # dùng vòng lặp
        # # lưu vào file 
        # file2 = open("test.txt",  encoding="utf8", mode ="a")
        # for i in range(len(data)):
        #     file2.write(data[i] + ",")
        # file2.write("\n")
        with open("clean_data.csv", "a", encoding="utf8", newline='') as file_csv:
            writer = csv.writer(file_csv)
            writer.writerow(data)
        
        
    except:
        print (sbd_str)





# # ########### test logical
# s = "<title>So giao duc</title>"

# tags = []

# for i in range (len(s)):
#     if s[i] == "<":
#         begin = i
#     elif s[i] == ">":
#         end = i    
#         tags.append(s[begin: end+1])
# for tag in tags:
#     s=  s.replace(tag, "")    

# print (s)




















