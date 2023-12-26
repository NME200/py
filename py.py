import time

while True:
    # 获取当前时间
    now = time.localtime()
    
    # 格式化时间显示
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", now)
    
    # 打印时间
    print(current_time)
    time.sleep(1)
