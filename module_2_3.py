my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
my_list_f = my_list[a]
while my_list_f >= 0 and a < len(my_list):
    my_list_f = my_list[a]
    a = a + 1
    if my_list_f < 0:
       break
    elif my_list_f == 0:
        continue
    print(my_list_f)

