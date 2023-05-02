from django.contrib import admin
from django.urls import path
from StudentEvaluation import views



admin.site.site_header = 'ACADEMIC EVALUATION ADMIN'
admin.site.site_title = 'ACADEMIC EVALUATION SYSTEM'
admin.site.index_title = 'ACADEMIC EVALUATION'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),

    path('register/', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),

    path('users/index/', views.index_view, name='index_view'),
    path('users/form', views.form, name='form'),
    
]