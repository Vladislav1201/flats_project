import time

def download_report():
    print("Начинаю скачивание отчета...")
    # Имитируем блокирующую операцию (ожидание ответа от сервера)
    time.sleep(2)
    print("Отчет скачан.")

def process_data():
    print("Начинаю обработку данных...")
    # Имитируем блокирующую операцию (сложные вычисления или обработка)
    time.sleep(3)
    print("Данные обработаны.")

def save_results():
    print("Начинаю сохранение результатов...")
    # Имитируем блокирующую операцию (запись на диск)
    time.sleep(1)
    print("Результаты сохранены.")

# --- Основная часть программы ---
print("Запуск программы.")
start_time = time.time()

download_report()
process_data()
save_results()

end_time = time.time()
total_time = end_time - start_time
print(f"Программа завершена за {total_time:.2f} секунд.")
