def rot(name,sid,letter_list):
    my_list = []
    for i in range(len(name)):
        index = (letter_list.index(name[i]) + int(sid[i]))%26
        my_list.append(letter_list[index])
    return ''.join(my_list)
