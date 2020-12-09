def get_all():
    format_option_in = input()  # 输入的格式化选项
    options_no_para = []  # 无参选项
    options_para = []  # 带参选项
    # 第一个到倒数第一个
    for i in range(len(format_option_in) - 1):
        if format_option_in[i] != ':':
            if format_option_in[i + 1] == ':':
                options_para.append('-' + format_option_in[i])
                i += 1
            else:
                options_no_para.append('-' + format_option_in[i])
    # 倒数第一个
    options_no_para.append('-' + format_option_in[-1])
    # print(options_no_para)
    # print(options_para)

    num = int(input())
    for i in range(num):
        dic = {}  # 选项-参数字典，无参选项的值为空
        command = input().split(' ')
        # print(command)
        output = 'Case ' + str(i + 1) + ': '
        # 第二个到倒数第二个:
        j = 1
        # for j in range(1, len(command) - 1): 不知道为什么在if里用j += 1不能跳过参数
        while j < len(command) - 1:
            if command[j] in options_para:
                dic[command[j]] = command[j + 1]
                j += 1
            elif command[j] in options_no_para:
                # if command[j + 1] in options_no_para or command[j + 1] in options_para:
                dic[command[j]] = ''
            else:
                break
            j += 1
        # 倒数第一个
        if j == len(command) - 1:
            if command[-1] in options_no_para:
                dic[command[-1]] = ''
        # print(dic)
        # 这个是对字典进行排序，第一次只得了20分就是因为没排序，这个排序方法还是要记一下的
        ans = sorted(dic.items(), key=lambda x: x[0])
        new_dic = {i[0]: i[1] for i in ans}
        for key, value in new_dic.items():
            if value != '':
                output += key + ' ' + value + ' '
            if value == '':
                output += key + ' ' + value
        print(output)


get_all()
