def get_all():
    isbn_in = input('')
    tmp = isbn_in.split('-')
    # print(tmp)
    if tmp[3] != 'X':
        indication_code = int(tmp[3])  # 标识码
    else:
        indication_code = 'X'
    # print(indication_code)
    sum_value = int(tmp[0]) + int(tmp[1][0]) * 2 + int(tmp[1][1]) * 3 + int(tmp[1][2]) * 4 + int(tmp[2][0]) * 5 + int(
        tmp[2][1]) * 6 + int(tmp[2][2]) * 7 + int(tmp[2][3]) * 8 + int(tmp[2][4]) * 9
    mod_value = sum_value % 11
    if mod_value == 10:
        mod_value = 'X'
    if mod_value == indication_code:
        print('Right')
    else:
        isbn_out = isbn_in
        isbn_out = isbn_out.rstrip(tmp[3])
        isbn_out += (str(mod_value))
        print(isbn_out)


get_all()
