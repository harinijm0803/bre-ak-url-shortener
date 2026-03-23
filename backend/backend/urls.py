from django.contrib import admin
from django.urls import path
from shortener import views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.dashboard, name="dashboard"),

    path('create/', views.create_page, name="create_page"),

    path('generate/', views.create_url, name="create_url"),

    path('delete/<int:url_id>/', views.delete_url, name="delete_url"),

    path('<str:short_code>/', views.redirect_short, name="redirect_short"),
]
