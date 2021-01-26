from django.urls import path, include
from. import views

urlpatterns = [
    path('', views.home, name="home"),
    path('comp-profil', views.completeProfil, name="profil"),
    path('connexion/', views.connexion, name="connexion"),
    path('inscription/', views.register, name="inscription"),
    path('deconnexion/', views.deconnexion, name="deconnexion"),
    #path('payement', views.payement, name="payement"),
    #path('deconnexion', views.deconnexion, name="deconnexion"),
    #path('connexion', views.connexion, name="connexion"),
    #path('vue-payments', views.vue, name="vuepay"),
]
