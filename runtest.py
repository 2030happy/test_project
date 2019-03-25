import unittest, time
from test_case import test_baidu, test_youdao
from HTMLTestRunner import HTMLTestRunner

# 指定测试用例为当前文件夹下的test_case目录
test_dir = './test_case'

discover = unittest.defaultTestLoader.discover(test_dir,
                                               pattern='test_*.py')

if __name__ == '__main__':

    now = time.strftime("%y-%m-%d %H_%M_%S")
    filename = test_dir + '/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description='用例执行情况：')
    runner.run(discover)
    fp.close()

"""
if __name__ == "__main__":
    discover = unittest.defaultTestLoader.discover("./test_case/",
                                                   pattern="test_*.py")
    runner = unittest.TextTestRunner()
    runner.run(discover)

"""

"""
#discover = unittest.defaultTestLoader.discover("./test_case/",
#pattern="test_*.py")
suite = unittest.TestSuite()
suite.addTest(test_baidu.MyTest("test_baidu"))
suite.addTest(test_youdao.MyTest("test_youdao"))

runner = unittest.TextTestRunner()
runner.run(suite)
"""