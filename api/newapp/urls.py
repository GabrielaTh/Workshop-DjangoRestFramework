from django.urls import path, include

from rest_framework.authtoken import views as auth_views
from rest_framework.routers import DefaultRouter, SimpleRouter

from . import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('incidents', views.IncidentsViewSet)
router.register('detail', views.DetailViewSet)
router.register('Transports', views.TransportsViewSet)
router.register('TypeIncidents', views.TypeIncidentsViewSet)
router.register('Motivation', views.MotivationViewSet)
router.register('Periode', views.PeriodeViewSet)
router.register('Group', views.GroupViewSet)
urlpatterns = [
    path('', include(router.urls)),
]