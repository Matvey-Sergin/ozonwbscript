import os

# Путь к папке с твоими картинками (точка означает текущую папку)
folder_path = "."


def rename_files_to_lower():
    files = os.listdir(folder_path)
    count = 0

    for filename in files:
        # Проверяем, что это картинка (png или jpg)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            old_path = os.path.join(folder_path, filename)

            # Делаем имя маленькими буквами
            new_name = filename.lower()
            new_path = os.path.join(folder_path, new_name)

            # Если имя изменилось (были большие буквы), переименовываем
            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f"✅ {filename} ---> {new_name}")
                count += 1

    print(f"\n🚀 Готово! Переименовано файлов: {count}")


if __name__ == "__main__":
    rename_files_to_lower()