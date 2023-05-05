def count_word_length(my_list):
    counter = 0
    for item in my_list:
        if len(item)>= counter:
            counter = len(item)
    return counter

temp_list=["hello","world","a","long","min"]
print("longest word count is %d" %count_word_length(temp_list))
            
