# -*- coding:utf-8 -*-
'''
SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
MIMEText函数，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'，最终的MIME就是'text/plain'，最后一定要用utf-8编码。
要发送HTML邮件，在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以.
带附件邮件，构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象
'''
'''
SMTP是用于发送电子邮件的协议，
而IMAP规定如何与电子邮件服务提供商的服务器通信，取回发送到你的电子邮件地址的邮件
'''
#----------------------------------------------------------发送纯文本邮件----------------------------------------------------------#
import smtplib
from email.mime.text import MIMEText

# 邮件发件方邮箱地址及密码
from_addr = 'caosainan@dafycredit.com'
password = 'Wj232261'
# 邮箱smtp服务器地址
smtp_server = 'email.dafycredit.com'
# 邮件接收方邮箱地址，多个接收人时用[]
to_addr = ['cenjiarong@dafycredit.com']

# 设置email内容信息
message = MIMEText('123 456 789', 'plain', 'utf-8')
# 邮件主题
message['Subject'] = 'caosainan'
# 发送方信息
message['From'] = from_addr
# 接受方信息
message['To'] = to_addr[0]

# 登录邮箱发送邮件
try:
    # 连接到服务器
    server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
    # server.set_debuglevel(1)  # 就可以打印出和SMTP服务器交互的所有信息
    # 登录邮箱
    server.login(from_addr, password)
    # 发送邮件
    # as_string()把MIMEText对象变成str
    server.sendmail(from_addr, to_addr, message.as_string())
    # 退出
    server.quit()
    print('success')
except smtplib.SMTPException as e:
    print('error', e)  # 打印错误

#----------------------------------------------------------发送HTML邮件----------------------------------------------------------#
# import smtplib
# from email.mime.text import MIMEText

# # 邮件发件方邮箱地址及密码
# from_addr = 'caosainan@yatang.cn'
# password = '215875Csn'
# # 邮箱smtp服务器地址
# smtp_server = 'smtp.yatang.com.cn'
# # 邮件接收方邮箱地址，多个接收人时用[]
# to_addr = ['1527604318@qq.com']

# # 设置email内容信息
# message = MIMEText('<html><body><h1>Hello</h1>' +
#                    '<p>send by <a href="http://www.python.org">Python</a>...</p>' + '</body></html>', 'html', 'utf-8')
# # 邮件主题
# message['Subject'] = 'caosainan'
# # 发送方信息
# message['From'] = from_addr
# # 接受方信息
# message['To'] = to_addr[0]

# # 登录邮箱发送邮件
# try:
#     # 连接到服务器
#     server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
#     # server.set_debuglevel(1)  # 就可以打印出和SMTP服务器交互的所有信息
#     # 登录邮箱
#     server.login(from_addr, password)
#     # 发送邮件
#     # as_string()把MIMEText对象变成str
#     server.sendmail(from_addr, to_addr, message.as_string())
#     # 退出
#     server.quit()
#     print('success')
# except smtplib.SMTPException as e:
#     print('error', e)  # 打印错误

#----------------------------------------------------------发送含有附件的邮件----------------------------------------------------------#
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart  # 处理多种形态的邮件主体
# from email.mime.image import MIMEImage  # 处理图片
# # from email.mime.image import MIMEBase

# # 设置登录及服务器信息
# from_addr = 'caosainan1@163.com'
# password = '8921920508csn'
# smtp_server = 'smtp.163.com'
# to_addr = ['1527604318@qq.com']

# # 设置eamil信息
# # 添加一个MIMEmultipart类，处理正文及附件
# message = MIMEMultipart()
# message['From'] = from_addr
# message['To'] = to_addr[0]
# message['Subject'] = 'caosainan'
# # 推荐使用html格式的正文内容，这样比较灵活，可以附加图片地址，调整格式等
# with open('abc.html', 'r') as f:
#     content = f.read()
# # 设置html格式参数
# part1 = MIMEText(content, 'html', 'utf-8')

# # 添加一个txt文本附件
# with open('abc.txt', 'r')as h:
#     content2 = h.read()
# # 设置txt参数
# part2 = MIMEText(content2, 'plain', 'utf-8')
# # 附件设置内容类型，方便起见，设置为二进制流
# part2['Content-Type'] = 'application/octet-stream'
# # 设置附件头，添加文件名
# part2['Content-Disposition'] = 'attachment;filename="abc.txt"'

# # 添加excel文件
# with open('abc.xlsx', 'r') as r:
#     content3 = r.read()
# part3 = MIMEText(content3, 'plain', 'utf-8')
# part3['Content-Type'] = 'application/octet-stream'
# part3['Content-Disposition'] = 'attachment;filename="abc.xlsx"'

# # 添加照片附件
# with open('abc.png', 'rb')as fp:
#     picture = MIMEImage(fp.read())
#     # 与txt文件设置相似
#     picture['Content-Type'] = 'application/octet-stream'
#     picture['Content-Disposition'] = 'attachment;filename="abc.png"'
# # 将内容附加到邮件主体中
# message.attach(part1)
# message.attach(part2)
# message.attach(part3)
# message.attach(picture)


# # 登录并发送
# try:
#     smtpObj = smtplib.SMTP(smtp_server, 25)
#     smtpObj.login(from_addr, password)
#     smtpObj.sendmail(
#         from_addr, to_addr, message.as_string())
#     print('success')
#     smtpObj.quit()
# except smtplib.SMTPException as e:
#     print('error', e)

#--------------------------------------------自动定时发送邮件--------------------------------------------------#
