from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import calculator.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', calculator.views.index),
    url(r'^get_zipcode$', calculator.views.zipcode_info),
    url(r'^get_bounds$', calculator.views.bounds_info),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^get_neighbors$', calculator.views.cbsa_from_zipcode),
    url(r'^check_zipcode$', calculator.views.check_zipcode_exist),
]
