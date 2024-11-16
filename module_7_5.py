import os

directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getatime(filepath)
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.getsize(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,  Родительская директория: {parent_dir}')