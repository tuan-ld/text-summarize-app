from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'app.views.index'),
    url(r'^app/$', 'app.views.landing_view'),
    url(r'^admin/', include(admin.site.urls)),
]
