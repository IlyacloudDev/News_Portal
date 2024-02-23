import os
from celery import Celery


# связываем настройки Django с настройками Celery через меременную окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'News_Portal.settings')

# создаём экземпляр приложения Celery и устанавливаем для него файл конфигурации
# мы также указываем пространство имён, чтобы Celery сам находил все необходимые настройки в общем конфигурационном
# файле settings.py
app = Celery('News_Portal')
app.config_from_object('django.conf:settings', namespace='CELERY')

# указываем Celery автоматически искать задания в файлах tasks.py каждого приложения проекта
app.autodiscover_tasks()
