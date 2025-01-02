input_string = input('enter your text :')


input_string = input_string.strip('.')  


char_count_Dic = {}


for char in input_string:
    if char in char_count_Dic:
        char_count_Dic[char] += 1
    else:
        char_count_Dic[char] = 1


print(char_count_Dic.items())
# for n  in char_count_Dic.items():
#     print(f"{n}" )