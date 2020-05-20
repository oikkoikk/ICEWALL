# % operator
print('Hello %s %d!' % ('icewall', 2020))

# str.format
print('Hello {} {}!'.format('icewall', 2020))

# f-string
name = 'icewall'
year = 2020
print(f'Hello {name} {year}')

# 기존 방식들과 비슷하게 사용 가능하다
num = 0.123456789
print('num: %.5f' % num)
print('num: {:.5f}'.format(num))
print(f'num: {num:.5f}')
# num: 0.12346
