from django.urls import path

from testapi.views import (index,
                           contact,
                           blog,
                           about,
                           support)

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('support/', support, name='support'),
]