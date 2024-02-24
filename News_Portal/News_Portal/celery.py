import os
import django
from celery import Celery
from celery.schedules import crontab


# связываем настройки Django с настройками Celery через меременную окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'News_Portal.settings')

django.setup()


from subscriptions.tasks import weekly_email


# создаём экземпляр приложения Celery и устанавливаем для него файл конфигурации
# мы также указываем пространство имён, чтобы Celery сам находил все необходимые настройки в общем конфигурационном
# файле settings.py
app = Celery('News_Portal')
app.config_from_object('django.conf:settings', namespace='CELERY')

# указываем Celery автоматически искать задания в файлах tasks.py каждого приложения проекта
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'sending_email_every_monday_8am': {
        'task': 'subscriptions.tasks.weekly_email',
        'schedule': crontab(minute='0', hour='8', day_of_week='saturday')
    }
}
