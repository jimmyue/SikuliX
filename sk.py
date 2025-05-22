# https://blog.csdn.net/abu935009066/article/details/131328693
# SikulixIDE执行代码
import test # 导入同目录python脚本(PYTHON的包sikulix不能直接导入，所以要用python写)

# 调用特定函数并传参
result_add = test.int_add("5","4")
result_str = test.str_add("ca", "lc")
print(result_add,result_str)     

# 操作计算器计算
type("r",Key.WIN)  #按WIN+R健
paste(result_str)
type(Key.ENTER)
wait(2)
paste("1+2")
wait(1)
type(Key.ENTER)
