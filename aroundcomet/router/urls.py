from .views import Test
from django.conf.urls import url , include

urlpatterns = [
                url(r'^tes$', Test.as_view(), name='tes'),
                ]
