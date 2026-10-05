# Blogicum

Учебный проект «Блогикум», часть 2: публикации из базы данных.
Создан на основе официального репозитория yandex-praktikum/django_sprint3.

## Запуск в Windows (PowerShell)

Команды выполняются из папки django_sprint3. Используйте Python 3.10
для совместимости с зависимостями Практикума.

```powershell
py -3.10 -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe blogicum\manage.py migrate
.\venv\Scripts\python.exe blogicum\manage.py loaddata db.json
.\venv\Scripts\python.exe blogicum\manage.py runserver
```

На этом компьютере окружение уже установлено, миграции применены и
фикстуры загружены. Для запуска достаточно последней команды.
Откройте http://127.0.0.1:8000/.

Для входа в админку http://127.0.0.1:8000/admin/ создайте свой аккаунт:

```powershell
.\venv\Scripts\python.exe blogicum\manage.py createsuperuser
```

## Проверки

```powershell
.\venv\Scripts\python.exe -m pytest
.\venv\Scripts\python.exe -m flake8 blogicum
.\venv\Scripts\python.exe blogicum\manage.py check
.\venv\Scripts\python.exe blogicum\manage.py makemigrations --check --dry-run
```

Главная показывает пять последних доступных публикаций. Будущие посты,
снятые с публикации посты и посты скрытых категорий недоступны.
Скрытая локация не скрывает пост; шаблоны показывают «Планета Земля».
Категория обязательна в форме создания поста, но после её удаления
связь становится NULL, как требует задание.

### Обязательная категория и удаление связанного объекта

Для `Post.category` в задании заданы два независимых требования:
категорию обязательно выбирать при создании публикации, а при удалении
категории сохранять публикацию и устанавливать её внешний ключ в NULL.
Поэтому поле имеет `on_delete=models.SET_NULL`, `null=True`, `blank=False`.
Все внешние ключи имеют явный `on_delete`.

Это соответствует официальному тесту `tests/test_post_model.py`,
который проверяет `('category', ForeignKey, {'null': True, 'blank': False})`.
Дополнительные тесты в `tests/test_category_validation.py` проверяют,
что форма отклоняет пустую категорию, а удаление категории сохраняет пост.

В документации Django `SET_NULL` требует `null=True`; параметр `blank`
управляет допустимостью пустого значения при валидации формы.
Установка `blank=True` здесь сделала бы категорию необязательной,
нарушив условие задания и официальный тест.

- [SET_NULL](https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.SET_NULL)
- [blank](https://docs.djangoproject.com/en/3.2/ref/models/fields/#blank)

## Сдача

Репозиторий: https://gitlab.praktikum-devops.ru/dydyvany11/django_sprint3.
Удалённый origin настроен на этот репозиторий; официальный стартовый
репозиторий Практикума сохранён как upstream.

Изменения отправляются командой `git push origin main`.
После ИИ-ревью скачайте ZIP из GitLab и прикрепите его на странице сдачи.
