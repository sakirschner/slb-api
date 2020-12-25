from django.urls import path, include
from rest_framework.routers import DefaultRouter

from group import views

router = DefaultRouter()
router.register('groups', views.GroupViewSet)

app_name = 'group'

urlpatterns = [
    path('', include(router.urls)),
    path('groups/<int:pk>/', views.GetGroupByIdView.as_view(), name='group'),
]