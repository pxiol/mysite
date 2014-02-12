from django.contrib import admin
from polls.models import Poll
from .views import inicio
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls')),
   	url(r'^admin/', include(admin.site.urls)),
    url(r'^$' , 'polls.views.inicio'),

)


