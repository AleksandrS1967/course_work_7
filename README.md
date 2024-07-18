# course_work_7

Habit-Assistant
API для Ассистента по привычкам. Создавайте свои собственные привычки 
или используйте общедоступные, за каждое выполнение - вознаграждение... 
Приложение работает с Telegram и периодически (раз в день) - делает рассылки

/	CRUD(create)	CRUD(read)	CRUD(update)	CRUD(delete)
Habit	+	+	+	+
Users	+	-	-	-
Используемый стек:

Код - Python
Веб-фреймворк Django
База данных - postgres
Используемые в проекте сторонние библиотеки находятся в requirements.txt в корне проекта
Рекомендации по запуску:

Клонируйте проект
Установите библиотеки из requirements.txt
Запустите Postgresql - настройки бызы лежат в переменной DATABASES по пути ..\config\settings.py 
(При желании для полного доступа к приложению + к админке) 
Добавьте супер юзера командой 'python manage.py csu' - по пути ..\users\management\commands\csu.py 
можно изменить данные этого пользователя
Переименуйте файл .env.sample в .env и заполните его своими данными
Запустите проект