"""
2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

count_str = 0

with open("Task_2.txt", "r", encoding="utf-8") as my_file:
    for line in my_file:
        print(line, end='')
        count_str += 1
        count_words_in_str = 0
        line_split = line.split()
        for word in line_split:
            count_words_in_str+=1
        print(f"Количество слов в строке {count_str}: {count_words_in_str}")    

print(f"\n Количество строк: = {count_str} \n")
