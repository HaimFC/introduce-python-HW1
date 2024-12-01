def check_neg_or_pos(num):
    dup_check_minus = 0
    for i in range(0, len(num)):
        if num[i] == "-":

            dup_check_minus = dup_check_minus + 1
    if dup_check_minus % 2 == 0:
        return 0
    else:
        return 1


def check_duplicate_dots(num):
    dup_check_dot = 0
    for i in range(0, len(num)):
        if num[i] == ".":
            dup_check_dot = dup_check_dot + 1
    if dup_check_dot > 1:
        return 0
    else:
        return 1


def check_if_float(num):
    for i in range(0, len(num)):
        if num[i] == ".":
            return 1
        else:
            return 0


def check_validation(num, string):
    if check_duplicate_dots(num) == 0:
        return 0
    else:
        temp_num = 0
        for i in range(0, len(num)):
            if string.find(num[i]) == -1:
                temp_num = temp_num + 1
        if temp_num == 0:
            if string == "0123456789.":
                if num[0] == "0":
                    return 0
                if check_if_float(num) == 1:
                    check_after_digit = num.split(".", -1)
                    for i in range(0, len(check_after_digit[1])):
                        if check_after_digit[1][i] != "0":
                            return 0
            return 1
        else:
            return 0


def check_if_vowel(str_ind):
    vowels = "aeiouy "
    if vowels.find(str_ind) == -1:
        return 1
    else:
        return 0


def question_number_one():
    str_input = input()
    str_len = len(str_input)
    sum_non_vowels = 0
    for i in range(0, str_len):
        if str_input[i].isalpha() is True:
            temp = check_if_vowel(str_input[i])
            if temp == 1:
                sum_non_vowels = sum_non_vowels + 1
            else:
                sum_non_vowels = sum_non_vowels
        else:
            sum_non_vowels = sum_non_vowels
    print(sum_non_vowels)


def question_number_two():
    x = input()
    n = input()
    if check_neg_or_pos(n) == 0:
        n = n.replace("-", "")
    else:
        n = n.replace("-", "")
        n = "-" + n
    if check_neg_or_pos(x) == 0:
        x = x.replace("-", "")
    else:
        x = x.replace("-", "")
        x = "-" + x

    taylor_sum = 0
    result_x = check_validation(x, "0123456789-.")
    result_n = check_validation(n, "0123456789.")
    if result_n != 0 and result_x != 0:
        for i in range(1, int(float(n)) + 1):
            taylor_sum = taylor_sum + (((-1)**(i+1))*((float(x)**i)/i))
        print(taylor_sum)
    else:
        print("error")


def question_number_three():
    input_string = input()
    input_split = input_string.split(" ", -1)
    upper_list = []
    lower_list = []

    for i in range(0, len(input_split)):
        if i % 2 == 0:
            upper_list.append(input_split[i].upper())
        else:
            lower_list.append(input_split[i].lower())

    upper_list.sort()
    lower_list.sort()
    lower_list.reverse()
    input_split.clear()
    input_split = upper_list + lower_list
    print(" ".join(input_split))


def question_number_four():
    input_number = input()
    sum_iterations = 0
    loop_num = 0

    while loop_num <= 500:
        input_reversed = ""
        for i in range(0, len(input_number)):
            input_reversed = input_reversed + input_number[len(input_number) - 1 - i]

        if int(input_number) != int(input_reversed):
            input_number = str(int(input_number) + int(input_reversed))
            loop_num = loop_num + 1
            sum_iterations = loop_num
        else:
            sum_iterations = loop_num
            loop_num = 501

    if sum_iterations >= 500:
        print(True)
    else:
        print(sum_iterations)


number_question = input()
if number_question == "1":
    question_number_one()
    exit()
elif number_question == "2":
    question_number_two()
    exit()
elif number_question == "3":
    question_number_three()
    exit()
elif number_question == "4":
    question_number_four()
    exit()
else:
    print("error")