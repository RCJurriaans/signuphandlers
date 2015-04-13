from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from codecultform.views import SignUpViewSet

#router = routers.DefaultRouter()
#router.register(r'signup', SignUpViewSet.as_view())

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #url(r'^', include(router.urls)),
    url(r'^signup/$', SignUpViewSet.as_view()),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
