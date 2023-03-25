from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello_view_set',views.HelloViewset,basename='hello_view_set')

urlpatterns = [
    path('hello_view/',views.HelloApiView.as_view()),
    path('',include(router.urls))
]

