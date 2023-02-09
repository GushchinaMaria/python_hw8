"""
3) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
with open("Task_3.txt", "r", encoding="utf-8") as my_file:
    f_obj = open("new_file.txt", "a", encoding="utf-8")
    for line in my_file:
        line_split = line.split()
        for word in line_split:
            match word:
                case "One":
                    line = "Один - 1"
                case "Two":
                    line = "Два - 2"
                case "Three":
                    line = "Три - 3"
                case "Four":
                    line = "Четыре - 4"

        f_obj.write(line)
        f_obj.write("\n")

    f_obj.close()
