lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 처음부터 끝까지
print(lst[:])
print(lst[:len(lst)])
print(lst[0:])
# lst[0]부터 lst[4]까지
print(lst[:5])
# 음수를 이용해 뒤부터 셀 수도 있다
print(lst[-5:])
# 처음부터 끝까지, 거꾸로
print(lst[::-1])
# 처음부터 끝까지, 짝수번째만
print(lst[::2])
