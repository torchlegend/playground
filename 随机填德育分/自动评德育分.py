import openpyxl
import random

workbook = openpyxl.load_workbook("a.xlsx") #改成你喜欢的名字

worksheet = workbook["Sheet1"]
print(worksheet)

random_score = [random.randint(88, 92) for _ in range(33)]  #分数区间88-92，33个人
print(random_score)

for i in range(len(random_score)):
    worksheet.cell(i + 2, 3, random_score[i]) # 行，列，分数

workbook.save('德育学生打分表.xlsx')