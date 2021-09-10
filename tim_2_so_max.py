lst = []
while True:
    try:
        n = int(input('Nhập số lượng các phần tử (n>=2): '))
    except ValueError:
        print('Không hợp lệ!')
        continue
    if n>= 2:
        break
    else:
        print('Số phần tử phải lớn hơn 2 !!!')
        continue

def xu_ly_lst(n):
    for i in range(n):
        lst.append(float(input(f'Nhập phần tử {i}: ')))
    print('List vừa nhập là: ',lst)

    lst.sort(reverse=True)
    print('Hai phần tử lớn nhất list vừa nhập là: ',lst[0], 'và' , lst[1])

xu_ly_lst(n)


