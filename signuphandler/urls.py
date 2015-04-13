from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from codecultform import views

router = routers.DefaultRouter()
router.register(r'signup', views.SignUpViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
