
from python_01.python_07 import read_case,api_fun,write_file
def test_fun(filename,sheetname):
    test_read = read_case(filename, sheetname)
    # print(test_read)   #得到一个列表，里面有13条字典类型的测试数据
    # 进行用例执行的时候，一条一条的读取里面的测试数据，然后把列表里的地址，请求数据以及期望值取出来。
    for num in test_read:  # 遍历列表数据,即把字典格式得测试数据从列表里取出来
        # print(num)
        test_id = num['case_id']
        test_excepted = num['excepted']  # 获取期望信息，后面用于和实际结果进行比对
        # print(test_excepted)
        test_url = num['url']  # 读取到的数据是字典类型，将字典里的地址取出来
        test_data = eval(num['data'])  # 取出data,但是取出出来的数据类型是字符串，，data必须传字典格式，所以得用eval()函数把字符串转换为字典
        # print(test_data)
        # print(type(test_data))
        test_excepted = eval(num['excepted'])
        # print(test_excepted)
        # 2已经将数据取出来，开始进行用例执行，调用用例执行函数
        test_result = api_fun(test_url, test_data)
        # print(test_result)
        # 执行了测试用例之后需要将预期结果与实际结果进行比较以此来判定测试是否通过，所以要先把返回得实际结果取出来，返回结果为字典格式，用dict[]进行取即可
        excepted_msg = test_excepted['msg']  # 获取期望的msg信息
        excepted_code = test_excepted['code']  # 获取期望的code信息
        result_msg = test_result['msg']  # 获取实际的msg信息
        result_code = test_result['code']  # 获取实际的code信息
        print(test_id)
        print('期望code为:{}'.format(excepted_code), 'msg为:{}'.format(excepted_msg))
        # print('msg为:{}'.format( excepted_msg))
        print('实际code为:{}'.format(result_code), 'msg为:{}'.format(result_msg))
        # print('msg为:{}'.format(result_msg))
        # 把实际code和msg与实际code和msg取出来之后，就可以进行判断,如果相等，测试用例表格写入，passed,如果失败，写入faile
        if result_code == excepted_code and result_msg == excepted_msg:
            print('第{}条测试用例通过'.format(test_id))
            write_file(filename, sheetname, test_id + 1, 8, 'Passed')  # 调用写入结果函数，将测试结果写入文件
        else:
            print('第{}条测试用例不通过'.format(test_id))
            write_file(filename, sheetname, test_id + 1, 8, 'Falile')  # 调用写入结果函数，将测试结果写入文件
#调用函数,定义一个变量接收函数返回值
# test_result = test_fun("C:\\Users\\Minotaur.Lee\\.jenkins\\workspace\\scb18Python自动化测试\\test_data\\test_case_api.xlsx",'login')   #写文件的绝对路径
# test_result = test_fun("C:\\Users\\Minotaur.Lee\\.jenkins\\workspace\\scb18Python自动化测试\\test_data\\test_case_api.xlsx",'register')   #注意路径要放在jenkins工作空间里面

test_result = test_fun("C:\\python_project\\python\\python\\test_data\\test_case_api.xlsx",'login')
test_result = test_fun("C:\\python_project\\python\\python\\test_data\\test_case_api.xlsx",'register')
print(test_result)