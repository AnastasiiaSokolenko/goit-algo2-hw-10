# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


def create_schedule(subjects, teachers):
    """
    Жадібний алгоритм покриття множини.
    Повертає список викладачів із призначеними предметами
    або None, якщо покриття неможливе.
    """
    uncovered_subjects = set(subjects)
    schedule = []

    while uncovered_subjects:
        best_teacher = None
        best_covered = set()

        for teacher in teachers:
            # Які предмети цей викладач може покрити зараз
            covered = teacher.can_teach_subjects & uncovered_subjects

            if not covered:
                continue

            if (
                best_teacher is None
                or len(covered) > len(best_covered)
                or (len(covered) == len(best_covered) and teacher.age < best_teacher.age)
            ):
                best_teacher = teacher
                best_covered = covered

        # Якщо не знайшли жодного викладача, що покриває нові предмети
        if best_teacher is None:
            return None

        # Призначаємо предмети
        best_teacher.assigned_subjects = best_covered
        schedule.append(best_teacher)

        # Видаляємо покриті предмети
        uncovered_subjects -= best_covered

        # Щоб не обирати того ж викладача повторно
        teachers.remove(best_teacher)

    return schedule


if __name__ == '__main__':
    # Множина предметів
    subjects = {
        'Математика',
        'Фізика',
        'Хімія',
        'Інформатика',
        'Біологія',
        # 'Англійська' # Для перевірки випадку неможливого покриття
    }

    # Створення списку викладачів
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com",
                {"Математика", "Фізика"}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com",
                {"Хімія", "Біологія"}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com",
                {"Інформатика", "Математика"}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com",
                {"Біологія", "Хімія"}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com",
                {"Фізика", "Інформатика"}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com",
                {"Біологія"})
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")