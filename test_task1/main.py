import os
import uuid


# a) Создание нового каталога
directory = "/Users/magomedmagomedov/PycharmProjects/test_task/task_1"
os.makedirs(directory, exist_ok=True)


# b) Создание 10 GUID-ов и файлов с названиями GUID
for i in range(1, 11):
    guid = str(uuid.uuid4())
    file_path = os.path.join(directory, f"{guid}.txt")
    with open(file_path, "w") as file:
        file.write(str(i))


# c) Чтение содержимого каталога и запись в исходный файл
input_file_path = os.path.join(directory, "исходный.txt")
with open(input_file_path, "w") as input_file:
    for file_name in os.listdir(directory):
        if file_name.endswith(".txt") and file_name!="исходный.txt":
            file_path = os.path.join(directory, file_name)
            with open(file_path, "r") as file:
                content = file.read()
                input_file.write(f"{file_name} {content}\n")


# d) Изменение файлов
for file_name in os.listdir(directory):
    if file_name.endswith(".txt") and file_name!="исходный.txt":
        old_file_path = os.path.join(directory, file_name)
        with open(old_file_path, "r") as file:
            content = file.read().strip()
            new_file_name = f"{content}.txt"
            new_file_path = os.path.join(directory, new_file_name)
            os.rename(old_file_path, new_file_path)
            # Запись названия старого файла в новый
            with open(new_file_path, "w") as new_file:
                new_file.write(file_name)


# e) Чтение преобразованных файлов и запись в новый файл
renamed_input_file_path = os.path.join(directory, "переименованный.txt")
with open(renamed_input_file_path, "w") as renamed_input_file:
    for file_name in os.listdir(directory):
        if file_name.endswith(".txt") and file_name!="исходный.txt" and file_name!="переименованный.txt":
            file_path = os.path.join(directory, file_name)
            with open(file_path, "r") as file:
                content = file.read()
                renamed_input_file.write(f"{file_name} {content}\n")
