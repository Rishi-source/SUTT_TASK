"""
URL configuration for MEDC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from app import views
from ChatMessage import view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.register,name="register"),
    path("check_user/",views.check_user,name="check_user"),
    path("user_login",views.user_login,name="user_login"),
    path('accounts/', include('allauth.urls'),name='social'),
    path("accounts/profile/",views.patient_dashboard,name="patient_dashboard"),
    path("edit_profile/",views.edit_profile,name="edit_profile"),
    path("user_logout/",views.user_logout,name="user_logout"),
    path("appointment/",views.create_appointment,name="appointment"),
    path("appointment_status/",views.appointment_status,name="appointment_status"),
    path("staff_dashboard/",views.staff_dashboard,name="staff_dashboard"),
    path("staff_edit_profile/",views.staff_edit_profile,name="staff_edit_profile"),
    path("staff_appointment/",views.staff_appointment,name="staff_appointment"),
    path("approve/",views.approve,name="approve"),
    path('chat/', view.chat_view, name='chat'),
    path('chat/<int:sender>/<int:receiver>/', view.message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>/', view.message_list, name='message-detail'),
    path('api/messages/', view.message_list, name='message-list'),
    path('patient_info/', views.patient_info, name='patient_info'),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
