#-*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#-----------------------------------------------------------------------------------------------------------#
# # Pandas生成excel，并增加sheet表
# """
# padas dataframe生成excel
# """


# def dataFrame2sheet(dataframe, excelWriter):

#     # DataFrame转换成excel中的sheet表
#     dataframe.to_excel(excel_writer=excelWriter,
#                        sheet_name="info1", index=None)
#     dataframe.to_excel(excel_writer=excelWriter,
#                        sheet_name="info2", index=None)
#     dataframe.to_excel(excel_writer=excelWriter,
#                        sheet_name="info3", index=None)

#     excelWriter.save()
#     excelWriter.close()

# """
# excel中新增sheet表
# """


# def excelAddSheet(dataframe, excelWriter):

#     book = load_workbook(excelWriter.path)
#     excelWriter.book = book
#     dataframe.to_excel(excel_writer=excelWriter,
#                        sheet_name="info5", index=None)
#     excelWriter.close()

# if __name__ == '__main__':

#     # 数据集
#     dataSet = [
#         {"姓名": "张三", "年龄": 23, "性别": "男"},
#         {"姓名": "李四", "年龄": 25, "性别": "男"},
#         {"姓名": "王五", "年龄": 21, "性别": "女"}
#     ]

#     # excelPath（存excel文件的路径及文件名）
#     excelPath = "D:\\python\\dataset.xlsx"

#     # 生成DataFrame（需要存入的数据集）
#     dataframe = pd.DataFrame(dataSet)

#     # 创建ExcelWriter 对象(建立excel表)
#     excelWriter = pd.ExcelWriter(excelPath, engine='openpyxl')

#     # #生成excel
#     # dataFrame2sheet(dataframe,excelWriter)

#     # excel中增加sheet
#     excelAddSheet(dataframe, excelWriter)

