f1 = open('hello.txt', 'w')
f1.write('hello world!')
# f1 스트림이 닫혔는가? False
print(f'f1.closed: {f1.closed}')
f1.close()
# f1 스트림이 닫혔는가? True
print(f'f1.closed: {f1.closed}')

try:
    f2 = open('hello2.txt', 'w')
    f2.write('hello word!')
    # 예상치 못한 오류
    raise Exception('Error f2')
    f2.close()
except Exception as e:
    # Exception Handling
    print(e)
# f2 스트림이 닫혔는가? False
# resource leak 발생
print(f'f2.closed: {f2.closed}')
f2.close()

try:
    with open('hello3.txt', 'w') as f3:
        f3.write('hello word!')
        # 예상치 못한 오류
        raise Exception('Error f3')
except Exception as e:
    # Exception Handling
    print(e)
# f3 스트림이 닫혔는가? True
# resource leak 발생 안함
print(f'f3.closed: {f3.closed}')
