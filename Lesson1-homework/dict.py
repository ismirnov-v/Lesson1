# Комплексные типы данных. Словари:

temperature_data = {
    'city': 'Москва',
    'temperature': "20"
}

print(temperature_data["city"])

temperature_data["temperature"] = int(temperature_data["temperature"]) - 5
print(temperature_data)

print(f'Поиск ключа "country": {temperature_data.get("country")}')
print(temperature_data.get('country', 'Россия'))

temperature_data['date'] = '27.052019'
print(len(temperature_data))