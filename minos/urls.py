from django.urls import path, include
from. import views

urlpatterns = [
    path('', views.home, name="home"),
    path('connexion/', views.connexion, name="connexion"),
    path('inscription/', views.register, name="inscription"),
    path('profile/', views.register2, name="register2"),
    path('fac-step/', views.registerFac, name="registerFac"),
    path('inst-step/', views.registerInst, name="registerInst"),
    path('deconnexion/', views.deconnexion, name="deconnexion"),
    path('validated', views.validated, name="validated"),
    path('pending', views.pending, name="pending"),
    path('errors', views.errors, name="errors"),
    path('payements', views.payements, name="payements"),
    path('information', views.information, name="information"),
    path('profile', views.profile, name="profile"),
]
