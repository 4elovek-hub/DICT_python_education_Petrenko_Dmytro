import requests

# Кеш для збереження курсів
cache = {}

# Запит базової валюти (та, яку ви маєте)
base_currency = input().lower()

# Отримання курсу з сайту FloatRates
url = f"http://www.floatrates.com/daily/{base_currency}.json"
try:
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()
except Exception as e:
    print("Error fetching exchange rates:", e)
    exit()

# Автоматичне додавання курсів до кешу для USD та EUR, якщо вони не збігаються з базовою валютою
if base_currency != "usd" and "usd" in rates:
    cache["usd"] = rates["usd"]
if base_currency != "eur" and "eur" in rates:
    cache["eur"] = rates["eur"]

# Основний цикл запитів
while True:
    # Запит валюти, на яку обмінюємо
    target_currency = input().lower()
    if target_currency == "":
        break
    amount = float(input())

    print("Checking the cache...")

    # Перевірка кешу
    if target_currency in cache:
        print("It is in the cache!")
        rate = cache[target_currency]["rate"]
    else:
        print("Sorry, but it is not in the cache!")
        if target_currency in rates:
            cache[target_currency] = rates[target_currency]
            rate = rates[target_currency]["rate"]
        else:
            print("Currency not found!")
            continue

    # Розрахунок і виведення результату
    received_amount = round(amount * rate, 2)
    print(f"You received {received_amount} {target_currency.upper()}.")
