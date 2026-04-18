import pandas as pd

# Создаем 1000 строк с фейковыми артикулами
data = {
    'Артикул': [f'AUTO-{i}' for i in range(1, 1001)],
    'Название': [f'Запчасть тип {i}' for i in range(1, 1001)],
    'Ссылка на фото': ['' for _ in range(1000)] # Пустая колонка для нашего скрипта
}

df = pd.DataFrame(data)
df.to_excel('test_vladislav.xlsx', index=False)
print("Файл на 1000 строк готов! Гони его через свой основной скрипт.")