contacts = {
    "Anna": "093-123-45-67",
    "Ivan": "050-888-99-00",
    "Olha": "097-777-33-22"
}
contacts["Taras"] = "063-000-11-22"
del contacts["Ivan"]
print("Імена:", list(contacts.keys()))
print("Номера", list(contacts.values()))
print("Катя є в книзі:", "Katya" in contacts)


grades = {
    "math": 88,
    "physics": 75,
    "english": 93,
    "history": 59
}
best_subject = max(grades, key=grades.get)
print("Найвища оцінка з предмета:", best_subject)
average = sum(grades.values()) / len(grades)
print("Середній бал:", average)
high_scores = [subject for subject, mark in grades.items() if mark > 80]
print("Предмети з оцінкою > 80:", high_scores)


transactions = [
    ("Anna", 200),
    ("Ivan", -50),
    ("Anna", 100),
    ("Olha", 500),
    ("Ivan", 150),
    ("Olha", -100),
]
balances = {}
for name, amount in transactions:
    balances[name] = balances.get(name, 0) + amount
    print("Баланси:", balances)
    richest = max(balances, key=balances.get)
print("Найбільший баланс у:", richest)
negatives = [name for name, bal in balances.items() if bal < 0]
print("Клієнти з від’ємним балансом:", negatives)


text = "hello world hello again hello world test world"
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
    print("Кількість слів:", word_count)



    student = {
    "name": "Anna",
    "age": 20,
    "courses": ["math", "physics", "english"]
}
    import json
    json_string = json.dumps(student)
print("JSON-рядок:", json_string)
student_dict = json.loads(json_string)
student_dict["courses"].append("history")
print("Оновлений словник:", student_dict)