from filemanager import FileManager  # Импортируем класс FileManager из модуля filemanager

def test_create_file():
    file_manager = FileManager()

    # Тестирование функции создания файла
    file_name = "test.txt"
    file_manager.create_file(file_name)

    # Проверка, что файл создан успешно
    assert file_manager.file_exists(file_name)



