from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('health_record/', views.health_record, name='health_record'),
    path('calorie_intake/', views.calorie_intake, name='calorie_intake'),
    path('activity_log/', views.activity_log, name='activity_log'),

]