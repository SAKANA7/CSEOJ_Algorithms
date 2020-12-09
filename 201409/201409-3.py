def get_all():
    key_in = input()
    option = int(input())  # 0不敏感，1敏感
    num = int(input())
    strings = ['' for _ in range(105)]
    # print(key_in)
    if option == 1:
        for i in range(num):
            strings[i] = input()
        for i in range(num):
            if key_in in strings[i]:
                print(strings[i])
    elif option == 0:
        for i in range(num):
            strings[i] = input()
        for i in range(num):
            if key_in.lower() in strings[i].lower():
                print(strings[i])


get_all()
