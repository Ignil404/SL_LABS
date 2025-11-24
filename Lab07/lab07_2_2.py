import json
from collections import defaultdict

def read_json_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print("СОДЕРЖИМОЕ JSON ФАЙЛА:")
        print(json.dumps(data, indent=2, ensure_ascii=False))
        
        return data
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
        return {}

def find_customers_by_id_pattern(customers, pattern):
    found = [c for c in customers if pattern.lower() in c['customer_id'].lower()]
    
    print(f"ПОИСК КЛИЕНТОВ ПО ПАТТЕРНУ '{pattern}':")
    print(f"Найдено клиентов: {len(found)}")
    for c in found:
        print(f"  - {c['name']} (ID: {c['customer_id']}, Email: {c['email']})")
    
    return found

def count_customers_by_city(customers):
    city_counts = defaultdict(int)
    for c in customers:
        city_counts[c['city']] += 1
    
    print("КОЛИЧЕСТВО КЛИЕНТОВ ПО ГОРОДАМ:")
    for city, count in sorted(city_counts.items()):
        print(f"  {city}: {count}")
    
    return dict(city_counts)

def calculate_avg_loyalty_points(customers):
    if not customers:
        return 0
    
    total = sum(c['loyalty_points'] for c in customers)
    avg = total / len(customers)
    
    print("СРЕДНИЕ БОНУСНЫЕ БАЛЛЫ:")
    print(f"Среднее количество баллов: {avg:.2f}")
    
    return avg

def filter_and_save_customers(customers, output_filename, min_orders=10):
    filtered = [c for c in customers if c['total_orders'] >= min_orders]
    
    output_data = {
        'filtered_customers': filtered,
        'filter_criteria': f'total_orders >= {min_orders}',
        'total_count': len(filtered)
    }
    
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        
        print(f"ОТФИЛЬТРОВАННЫЕ ДАННЫЕ СОХРАНЕНЫ В {output_filename}:")
        print(f"Критерий фильтрации: количество заказов >= {min_orders}")
        print(f"Отфильтровано клиентов: {len(filtered)}")
        for c in filtered:
            print(f"  - {c['name']}: {c['total_orders']} заказов, {c['loyalty_points']} баллов")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")
    
    return filtered

def main():
    data = read_json_file('3.json')
    
    if data and 'customers' in data:
        customers = data['customers']
        
        find_customers_by_id_pattern(customers, 'abc')
        count_customers_by_city(customers)
        calculate_avg_loyalty_points(customers)
        filter_and_save_customers(customers, 'out.json', min_orders=10)

if __name__ == "__main__":
    main()