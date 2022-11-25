# 2) Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input("Введите время в секундах:"))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds_formatted = (seconds % 3600) % 60

print(f"Время в формате чч:мм:сс : {hours}:{minutes}: {seconds_formatted}")
