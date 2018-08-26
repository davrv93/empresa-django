from django.conf.urls import url, include
from rest_framework import routers
from .views.departamento import DepartamentoViewSet

router = routers.DefaultRouter()
router.register(r'departamento', DepartamentoViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
