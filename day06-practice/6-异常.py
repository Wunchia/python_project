# Author Wunchia
# 2024年12月30日21时35分18秒
# wunchia@outlook.com
import traceback

#异常练习
import test_exception_module
def test01():
    try:
        num=int(input('输入整数'))
    except Exception as e:
        print(e)

def test02():
    try:
        test_exception_module.test()
    except ValueError:
        print('输入需为整数')
    except ZeroDivisionError:
        print('不可除零 ')
    except Exception as e:
        import traceback
        print('未知错误 %s' %e)
        tb=e.__traceback__
        while tb.tb_next:
            tb=tb.tb_next
        filename=tb.tb_frame.f_code.co_filename
        lineno=tb.tb_lineno
        func_name=tb.tb_frame.f_code.co_name
        print(f"异常发生的文件（模块）：{filename}")
        print(f"异常发生的行数：{lineno}")
        print(f"异常发生的函数：{func_name}")
    else:
        print('成功执行，结果为%d' %test_exception_module.result)
    finally:
        print('处理完成')

#异常传递
def demo01():
    num=int(input('enter int'))
    print('I am demo01')
    return num
def demo02(num):
    num=2/num
    print('I am demo02')
    return num
def test03():
    try:
        print(demo02(demo01()))
    except Exception as e:
        import traceback
        print('未知错误 %s' % e)
        tb = e.__traceback__
        while tb.tb_next:
            tb = tb.tb_next
        filename = tb.tb_frame.f_code.co_filename
        lineno = tb.tb_lineno
        func_name = tb.tb_frame.f_code.co_name
        print(f"异常发生的文件（模块）：{filename}")
        print(f"异常发生的行数：{lineno}")
        print(f"异常发生的函数：{func_name}")

#抛出异常
def pwd():
    pwd=str(input('输入密码'))
    if len(pwd)>=6:
        return pwd
    raise Exception('密码长度应大于6位')

def test04():
    try:
        print(pwd())
    except Exception as e:
        print(e)

if __name__ == '__main__':
  # test01()
  # test02()
  # test03()
  test04()