import os

# Название папки для тестовых фото
folder_name = 'test_photos'

# Создаем папку, если её нет
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Генерируем 1000 пустых файлов с именами AUTO-1.png, AUTO-2.png и т.д.
for i in range(1, 1001):
    file_name = f'AUTO-{i}.png'
    file_path = os.path.join(folder_name, file_name)

    # Создаем пустой файл
    with open(file_path, 'w') as f:
        pass

print(f"Готово! В папке '{folder_name}' теперь 1000 тестовых файлов.")