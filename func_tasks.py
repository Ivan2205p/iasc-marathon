def hello_world():
    print("Hello, world!")


def greet(name="Гість"):
    print(f"Привіт, {name}!")


def square(n):
    return n ** 2


def add(a, b):
    return a + b


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_even(n):
    return n % 2 == 0


def print_numbers(n):
    for i in range(1, n + 1):
        print(i)


def find_name(name, name_list):
    return name in name_list


def max_of_three(a, b, c):
    return max(a, b, c)

def reverse_string(s):
    return s[::-1]


def count_vowels(s):
    vowels = "аеєиіїоуюяAEIOUYaeiouy"
    return sum(1 for char in s if char in vowels)


def average(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def print_user_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


def outer():
    def inner():
        print("Я - вкладена функція!")
    inner()


hello_world()
greet("Anna")
print("Квадрат числа 5:", square(5))
print("Сума 3 і 4:", add(3, 4))
greet() 
print("Факторіал 5:", factorial(5))
print("Число 4 парне?", is_even(4))
print("Числа від 1 до 5:")
print_numbers(5)
print("Чи є 'Ivan' у списку?", find_name("Ivan", ["Anna", "Ivan", "Olha"]))
print("Максимальне з 3, 7, 2:", max_of_three(3, 7, 2))
print("Навпаки 'hello':", reverse_string("hello"))
print("Кількість голосних у 'hello world':", count_vowels("hello world"))
print("Середнє значення (3, 5, 8):", average(3, 5, 8))
print("Інформація про користувача:")
print_user_info(name="Anna", age=25, city="Kyiv")
print("Вкладена функція:")
outer()