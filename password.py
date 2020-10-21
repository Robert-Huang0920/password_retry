#密碼重試程式
password = 'a123456'
x = 3 #剩餘機會
while x >= 0:

    pwd = input('請輸入您的密碼：')
    if pwd == password:
        print('登入成功')
        break
    else:
        x = x - 1
        print('密碼錯誤！還有', x, '次機會！')
        if x == 0:
            print('密碼錯誤次數過多，請重新啟動')
            break