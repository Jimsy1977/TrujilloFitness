from django.urls import path
from authapp import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('signup',views.signup, name="signup"),
    path('login',views.handlelogin, name="handlelogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('contact',views.contact,name="contact"),
    path('join',views.inscripcion,name="Inscripcion"),
    path('perfil',views.perfil,name="perfil"),
    path('galeria',views.galeria,name="galeria"),
    path('asistencia',views.asistencia,name="asistencia"),
    path('historia',views.historia,name="historia"),
    path('servicios',views.servicios,name="servicios")
]
