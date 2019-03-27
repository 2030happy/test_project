import unittest, time, smtplib, os
from test_case import test_baidu, test_youdao
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header

# 定义发送邮件
def send_main(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')

    smtp = smtplib.SMTP()
    # 连接发送邮箱服务器
    smtp.connect("smtp.qq.com")
    # 登录发送邮箱
    smtp.login("username@qq.com", "SMTP授权码") #qancfhuunyuoihbe
    # 发送邮件（发送邮箱和接收邮箱地址）
    smtp.sendmail("username@qq.com", "receiver@163.com",
                  msg.as_string())
    smtp.quit()
    print('email has send out!')

# 查找测试报告目录，找到最新生成的测试报告文件
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':

    # 测试用例和测试报告路径
    test_dir = "./test_case"
    test_report = "./report"

    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern='test_*.py')
    # 生成测试html报告
    now = time.strftime("%y-%m-%d_%H_%M_%S")
    filename = test_report + '/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description='用例执行情况：')
    runner.run(discover)
    fp.close()

    # 获取最新测试报告
    new_report = new_report(test_report)
    # 发送最新测试报告邮件
    send_main(new_report)




"""
# 通过discover执行目录下所有的用例
if __name__ == "__main__":
    discover = unittest.defaultTestLoader.discover("./test_case/",
                                                   pattern="test_*.py")
    runner = unittest.TextTestRunner()
    runner.run(discover)

"""

"""
# 通过测试套件suite指定执行某个用例（或按顺序执行）
#discover = unittest.defaultTestLoader.discover("./test_case/",
#pattern="test_*.py")
suite = unittest.TestSuite()
suite.addTest(test_baidu.MyTest("test_baidu"))
suite.addTest(test_youdao.MyTest("test_youdao"))

runner = unittest.TextTestRunner()
runner.run(suite)
"""