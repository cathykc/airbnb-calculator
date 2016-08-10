from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import calculator.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', calculator.views.index),
    url(r'^db', calculator.views.db),
    url(r'^admin/', include(admin.site.urls)),
]
