from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /munkistore/applist
    url(r'^applist/$', views.applist, name='applist'),
    url(r'^purchased_apps/$', views.purchased_apps, name='purchased_apps'),
    url(r'^current_datetime/$', views.current_datetime),
    url(r'^usertest/$', views.usertest),
    url(r'^formtest/$', views.get_name),
]