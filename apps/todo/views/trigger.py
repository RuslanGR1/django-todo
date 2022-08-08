import logging

from django import views
from django.http import HttpResponse

from ..tasks import hello


class TriggerView(views.View):
    """Trigger class"""

    logger = logging.getLogger(__name__)

    def get(self, request):
        print("hi")

    # def get(self, request):
    #     """Run trigger"""
    #     hello.delay()
    #     return HttpResponse('OK')
