try:
    x = int('string')
except ValueError:
    print('ValueError 발생!')
else:
    print('Exception 없음!')
finally:
    print('무조건 실행됨!')

try:
    x = int('123')
except ValueError:
    print('ValueError 발생!')
else:
    print('Exception 없음!')
finally:
    print('무조건 실행됨!')
