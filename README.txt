
DbData - папка, в якій зберігаються бази даних та файли
із запитами до них.

 ======================================================
|----Будь ласка, зберігайте свої файли лише в DbData---|
 ======================================================

Файли з запитами підтримують лише *.csv

!Увага!
Запити в ваших файлах пишіть у подвійних лапках.
Приклад:
"SELECT * FROM USERS WHERE ID = 0"

"INSERT INTO USER (some_data, some_data1, some_data2)
VALUES (0, 1, 'some_data')"

Програма має невеликий термінал, в якому відображаються
як успішне виконання(результат запитів), так і помилки.

Програма має змогу створювати автоматично тестові бази даних,
на яких можна навчатись або тестувати.

Є можливість подивитись, чи успішно виконані запити із файлу,
оскільки є невеликий аутпут в правій частині програми.

Розрахована на невеликі бази даних.

Голова файлу - project.py

faker_data.py - файл, в якому створюється тестова база даних.

saver.py - файл, який допомогає працювати з базою даних через термінал.

selector.py - файл, який допомогає працювати із запитами, які є в
*.csv файлі.