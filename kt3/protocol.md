# Рабочий протокол «Медиаполка»

Автор, группа: Гзгзян Никита Александрович, ИТ-9.24.3-ДН. Дата: 14.11.2026. Требования: 1.0. Использованный Python: 3.12.13.

## 1. Короткий план до исправлений

Цель: обнаружить ошибочную обработку входных данных, проблемы с возвращением выдач.

Проверяем: границы допустимого количества оборудования, повторный возврат заявок, выдачу отсутствующего оборудования, ввод некорректных значений. За рамками: многопоточность, структура возвращаемых словарей.

Начнём с пустого состояния. Сначала проверим выдачу разного количества оборудования. Остановимся для разбора, если какой-либо тест упадёт. Починку считаем завершённой, когда все тесты успешны. Если время закончится раньше, остановимся на том, что сделали.

| № | Правило | Исходные данные и действие | Ожидание до запуска | Приоритет / причина | Имя теста или ручная проверка |
| --- | --- | --- | --- | --- | --- |

| 1 | R2 | `issue`, `mic`, `quantity=0` | `ok=False` | Высокий | `test_issue_zero_microphones` |
| 2 | R2 |  `issue`, `mic`, `quantity=1` | `ok=True` | Высокий | `test_issue_one_microphone` |
| 3 | R2 | `issue`, `mic`, `quantity=3` | `ok=True` | Высокий | `test_issue_three_microphones` |
| 4 | R2 | `issue`, `mic`, `quantity=4` | `ok=False` | Высокий | `test_issue_four_microphones` |
| 5 | R2 | `issue`, `mic`, `quantity=foo` | `ok=False` | Средний | `test_issue_foo_microphones` |
| 6 | R2 | `issue`, `mic`, `quantity=-2` | `ok=False` | Средний | `test_issue_minus_two_microphones` |
| 7 | R2 | `issue`, `mic`, `quantity=0.5` | `ok=False` | Средний | `test_issue_half_microphones` |
| 8 | R3 | `issue`, `tripod`, `quantity=2` | `ok=False` | Высокий | `test_issue_two_tripods` |
| 9 | R3 | `issue`, `tripod`, `quantity=1` (2 раза) | `ok=False` | Высокий | `test_issue_tripod_two_times` |
| 10 | R3 | `issue`, `light`, `quantity=1` | `ok=False` | Высокий | `test_issue_light` |
| 11 | R5 | `return`, `loan_id=-1` | `ok=False` | Средний | `test_return_invalid_loan` |
| 12 | R5 | `issue`, `mic`, `quantity=1` ; `return`, `loan_id=1` | `ok=True` | Высокий | `test_issue_and_return_microphone` |
| 13 | R6 | `issue`, `mic`, `quantity=1` ; `return`, `loan_id=1` ; `return`, `loan_id=1` | `ok=False` | Высокий | `test_issue_and_return_microphone_two_times` |
| 14 | R5 | `issue`, `tripod`, `quantity=1` ; `return`, `loan_id=1` ; `issue`, `tripod`, `quantity=1` | `ok=True` | Высокий | `test_issue_and_return_tripod_then_issue_again` |

## 2. Причины и исправления

### "3" не принимается в качестве корректного значения

- Правило, данные и шаги: R2, `mic`, `quantity=3`.
- Ожидалось / получилось до исправления: `ok=True`, успешная выдача / `ok=False`, неуспешная выдача.
- Обнаруживающий тест и файл вывода до исправления: `test_issue_three_microphones`, `before.txt`.
- Причина в коде и изменение: `if quantity < 1 or quantity >= 3` => `if quantity < 1 or quantity > 3`.
- Повторная и соседняя проверки: `after.txt`.

### Можно выдать больше оборудования, чем есть

- Правило, данные и шаги: R3, `tripod`, `quantity=2`.
- Ожидалось / получилось до исправления: `ok=False`, неуспешная выдача / `ok=True`, успешная выдача.
- Обнаруживающий тест и файл вывода до исправления: `test_issue_two_tripods`, `before.txt`.
- Причина в коде и изменение: `if available < 1` => `if available < quantity`.
- Повторная и соседняя проверки: `after.txt`.

### Можно повторно вернуть выдачу

- Правило, данные и шаги: R6, `mic`, `quantity=1`.
- Ожидалось / получилось до исправления: `ok=False`, неуспешный возврат / `ok=True`, успешный возврат.
- Обнаруживающий тест и файл вывода до исправления: `test_issue_and_return_microphone_two_times`, `before.txt`.
- Причина в коде и изменение: `if loan["id"] == loan_id:` => `if loan["id"] == loan_id and loan["status"] == "issued":`.
- Повторная и соседняя проверки: `after.txt`.

## 3. Итог

Команда финального запуска: `python3 -m unittest discover -s tests -v`. Обнаружено тестов: 15. Прошло / упало / ошибки: 15 / 0 / 0. Вывод сохранён в: after.txt.

Какие проверки появились после уточнения плана: -

Что осталось неисправленным или непроверенным: структура возвращаемых словарей; проверялась только `id`.

Техническая помощь с запуском/синтаксисом: -

Ответы на три вопроса задания:
1. Какой ваш тест обнаруживает причину, а не только повторяет удачный пример? `test_issue_and_return_microphone_two_times`
2. Какая соседняя проверка помогает убедиться, что исправление не слишком узкое? `test_issue_three_microphones`
3. Что вы пока не проверили и как это ограничивает итоговый вывод? Нет такого
