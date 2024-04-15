import random


# Генератор логинов
def generate_login(name="Nikita", surname="Semenov", cohort_number="7", domain="yandex.com"):
    return f"{name}{surname}{cohort_number}{random.randint(100, 999)}@{domain}"


# Генератор паролей
def generate_password(length=random.randint(6, 10)):
    password = ''.join(str(random.randint(0, 9)) for i in range(length))
    return password


# Постоянный пользователь в системе:
cred_login = 'NikitaSemenov7251@yandex.com'
cred_pass = '93585982'