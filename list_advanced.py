students = ["Anna", "Ivan", "Olha", "Taras", "Katya"]
grades = [95, 62, 47, 88, 53]
max_index = grades.index(max(grades))
top_student = students[max_index]
print("Найвища оцінка у студента:", top_student)
passed_students = [students[i] for i in range(len(grades)) if grades[i] > 60]
print("Студенти з оцінкою > 60:", passed_students)
failed_count = sum(1 for g in grades if g < 60)
print("Не склали іспит:", failed_count)



logs = ["ok", "error", "fail", "ok", "error", "warning", "ok", "fail"]
log_counts = {}
for log in logs:
    log_counts[log] = log_counts.get(log, 0) + 1
print("Кількість кожного типу повідомлень:", log_counts)
error_count = logs.count("error")
error_percent = (error_count / len(logs)) * 100
print(f"Відсоток error: {error_percent:.2f}%")



expenses = [
    ["Понеділок", 120],
    ["Вівторок", 80],
    ["Середа", 150],
    ["Четвер", 0],
    ["П’ятниця", 250],
    ["Субота", 300],
    ["Неділя", 200]
]
max_day = max(expenses, key=lambda x: x[1])[0]
print("Найбільші витрати були у:", max_day)
total = sum(day[1] for day in expenses)
print("Загальні витрати за тиждень:", total)
days_over_100 = [day[0] for day in expenses if day[1] > 100]
print("Дні з витратами понад 100 грн:", days_over_100)


products = [
    ["яблуко", 2, 12.5],
    ["банан", 5, 8.0],
    ["молоко", 1, 34.0],
    ["хліб", 2, 16.0]
]
total_price = sum(qty * price for _, qty, price in products)
print("Загальна сума чеку:", total_price)
most_expensive = max(products, key=lambda x: x[2])[0]
print("Найдорожчий товар:", most_expensive)
receipt_lines = [f"{name} - {qty * price} грн" for name, qty, price in products]
print("Список рядків для чеку:")
for line in receipt_lines:
    print(line)


    squares = [x**2 for x in range(1, 31) if x % 2 == 0 and x % 4 != 0 and x not in [10, 14, 18]]
print("Квадрати з умовою:", squares)