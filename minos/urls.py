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
    #path('payement', views.payement, name="payement"),
    #path('deconnexion', views.deconnexion, name="deconnexion"),
    #path('connexion', views.connexion, name="connexion"),
    #path('vue-payments', views.vue, name="vuepay"),
]
