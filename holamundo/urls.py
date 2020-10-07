from django.urls import path

from . import views
from django.conf.urls import include,url
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'carreras',views.CarreraViewSet)
router.register(r'paralelo',views.ParaleloViewSet)
router.register(r'estudiante',views.EstudianteViewSet)
router.register(r'carreras',views.DocenteViewSet)

urlpatterns = [
    path('',views.index,name='index'),
    url(r'^',include(router.urls)),
    url(r'^api-auth',include('rest_framework.urls', namespace='rest_framework'))

]