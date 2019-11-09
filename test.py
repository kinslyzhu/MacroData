#coding:utf-8 # 强制使用utf-8编码格式
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from email.mime.multipart import MIMEMultipart

my_sender='q3398863@qq.com'    # 发件人邮箱账号
my_pass = 'qqfkeqdqknizcbbd'              # 发件人邮箱密码(当时申请smtp给的口令)
my_user='zhaoyunhe17@126.com'   # 收件人邮箱账号，我这边发送给自己


def mail():
    ret=True
    try:
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = my_sender
        message['To'] = my_user
        message['Subject'] = Header("Macro Watch", 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText('来来来，这是邮件的正文', 'plain', 'utf-8'))

        # 构造附件3（附件为HTML格式的网页）
        att3 = MIMEText(open('2019-09-30.html', 'rb').read(), 'base64', 'utf-8')
        att3["Content-Type"] = 'application/octet-stream'
        att3["Content-Disposition"] = 'attachment; filename="2019-09-29.html"'
        message.attach(att3)

        #
        # msg=MIMEText('填写邮件内容','plain','utf-8')
        # msg['From']=formataddr(["发件人昵称",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        # msg['To']=formataddr(["收件人昵称",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        # msg['Subject']="邮件主题-测试"                # 邮件的主题，也可以说是标题

        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.set_debuglevel(2)
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,my_user,message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()# 关闭连接
    except smtplib.SMTPException as e:# 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
        print(e)
    return ret

ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")