import openpyxl
import os

# ==========================================
# ⚙️ БЛОК НАСТРОЕК (БРОНЕБОЙНЫЙ v1.3)
# ==========================================
INPUT_FILE = "Футболки ВБ.xlsx"
OUTPUT_FILE = "READY_FOR_WB.xlsx"
BASE_URL = "https://raw.githubusercontent.com/Matvey-Sergin/ozonwbscript/main/"

SKU_COL = "B"
PHOTO_COL = "H"
START_ROW = 5
FILE_EXT = ".png"  # Проверь, что на Гитхабе именно .png маленькими буквами


# ==========================================
# 🚀 ДВИЖОК С АВТО-ИСПРАВЛЕНИЕМ
# ==========================================
def process_excel():
    print(f"🔧 Запуск PIM-Движка v1.3...")

    if not os.path.exists(INPUT_FILE):
        print(f"❌ Файл '{INPUT_FILE}' не найден!")
        return

    wb = openpyxl.load_workbook(INPUT_FILE)
    sheet = wb.active

    for row in range(START_ROW, sheet.max_row + 1):
        sku_val = sheet[f"{SKU_COL}{row}"].value
        if sku_val:
            # МАГИЯ ЗДЕСЬ:
            # 1. .strip() - убирает пробелы
            # 2. .lower() - делает ВСЕ буквы маленькими (и русские, и английские)
            # 3. .replace() - на всякий случай меняет английскую B на русскую в,
            # чтобы у тебя всегда был один стандарт.
            sku = str(sku_val).strip().lower().replace('b', 'в')

            # Собираем финальную ссылку
            final_url = f"{BASE_URL}{sku}{FILE_EXT}"
            sheet[f"{PHOTO_COL}{row}"] = final_url
            print(f"🔗 Ссылка для {sku_val} -> {final_url}")

    wb.save(OUTPUT_FILE)
    print("-" * 30)
    print(f"🎉 Готово! Проверяй файл: {OUTPUT_FILE}")


if __name__ == "__main__":
    process_excel()