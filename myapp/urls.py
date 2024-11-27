from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'branches', InfoCUBranchViewSet)
router.register(r'products', InfoProductViewSet)
router.register(r'histories', HistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_user, name='login_user'),
    path('report/', report, name='report'),
    path('filter/', filter_history, name='filter_history'),
]
