import csv
from collections import defaultdict


def read_csv_file(filename):
    students = []
    print("СОДЕРЖИМОЕ CSV ФАЙЛА:")
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            for i, row in enumerate(reader, 1):
                print(f"\nСтудент #{i}:")
                for key, value in row.items():
                    print(f"  {key} → {value}")
                students.append(row)
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
        return []
    
    return students

def find_student_min_max_physics(students):
    if not students:
        return None, None
    
    max_student = max(students, key=lambda s: int(s['Physics']))
    min_student = min(students, key=lambda s: int(s['Physics']))
    
    print("СТУДЕНТЫ С МИН/МАКС БАЛЛОМ ПО PHYSICS:")
    print(f"Максимальный балл: {max_student['FullName']} - {max_student['Physics']} баллов")
    print(f"Минимальный балл: {min_student['FullName']} - {min_student['Physics']} баллов")
    
    return max_student, min_student

def count_students_high_computer_science(students):
    count = sum(1 for s in students if int(s['Computer Science']) >= 80)
    
    print("СТУДЕНТЫ С ВЫСОКИМ БАЛЛОМ ПО COMPUTER SCIENCE (>= 80):")
    print(f"Количество студентов: {count}")
    print("\nСписок студентов:")
    for s in students:
        if int(s['Computer Science']) >= 80:
            print(f"  - {s['FullName']}: {s['Computer Science']} баллов")
    
    return count

def calculate_average_literature(students):
    if not students:
        return 0
    
    total = sum(int(s['Literature']) for s in students)
    avg = total / len(students)
    
    print("СРЕДНИЙ БАЛЛ ПО LITERATURE:")
    print(f"Средний балл: {avg:.2f}")
    
    return avg

def calculate_group_averages(students):
    groups = defaultdict(lambda: {'Math': [], 'Physics': [], 'Computer Science': [], 'Literature': []})
    
    for s in students:
        group = s['Group']
        groups[group]['Math'].append(int(s['Math']))
        groups[group]['Physics'].append(int(s['Physics']))
        groups[group]['Computer Science'].append(int(s['Computer Science']))
        groups[group]['Literature'].append(int(s['Literature']))
    
    print("СРЕДНИЕ БАЛЛЫ ПО ПРЕДМЕТАМ ДЛЯ КАЖДОЙ ГРУППЫ:")
    
    result = {}
    for group, subjects in sorted(groups.items()):
        print(f"\nГруппа {group}:")
        result[group] = {}
        for subject, scores in subjects.items():
            avg = sum(scores) / len(scores)
            result[group][subject] = round(avg, 2)
            print(f"  {subject}: {avg:.2f}")
    
    return result

def main():
    students = read_csv_file("3.csv")
    
    if students:
        find_student_min_max_physics(students)
        count_students_high_computer_science(students)
        calculate_average_literature(students)
        calculate_group_averages(students)
    
if __name__ == "__main__":
    main()