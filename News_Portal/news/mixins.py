import pytz

from django.utils import timezone
from django.shortcuts import redirect


class TimezoneMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['current_time'] = timezone.localtime(timezone.now())
        context['timezones'] = pytz.common_timezones
        return context

    # по пост-запросу будем добавлять в сессию часовой пояс,
    # который и будет обрабатываться написанным нами ранее middleware
    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect(self.request.path)
