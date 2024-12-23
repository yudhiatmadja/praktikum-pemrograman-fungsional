random_list = [900, 3.1, 3078, "Hello", 737, "Python", 2.7, 2002, 50,
               "Tech Winter", 7.566, 40, 1, "Is", 60.5, "Better", 1000.1,
               4, "world", 412, 5.5, "AI", 99.234, 12000]

float_tuple = ()
string_list = []
int_dict = {'satuan': [], 'puluhan': [], 'ratusan': [], 'ribuan': []}

for data in random_list:
    if isinstance(data, float):
        float_tuple += (data,)
    elif isinstance(data, str):
        string_list.append(data)
    elif isinstance(data, int):
        if data < 10:
            int_dict['satuan'].append(data)
        elif 10 <= data < 100:
            int_dict['puluhan'].append(data)
        elif 100 <= data < 1000:
            int_dict['ratusan'].append(data)
        elif data >= 1000:
            int_dict['ribuan'].append(data)

print("Float tuple:", float_tuple)
print("String list:", string_list)
print("Integer dictionary:", int_dict)
