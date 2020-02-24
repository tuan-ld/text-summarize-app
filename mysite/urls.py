from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'app.views.index'),
    url(r'^app/$', 'app.views.landing_view'),
    url(r'^admin/', include(admin.site.urls)),
]
