import os

class FileManager:
    def create_file(self, file_name):
        # Создание файла
        with open(file_name, 'w') as file:
            file.write('Test content')

    def file_exists(self, file_name):
        # Проверка существования файла
        return os.path.isfile(file_name)

