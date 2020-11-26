from django.urls import path, include
from. import views
from schema_graph.views import Schema

urlpatterns = [
    path('', views.home, name="home"),
    path('inscription', views.inscription, name="inscription"),
    path('payement', views.payement, name="payement"),
    path('deconnexion', views.deconnexion, name="deconnexion"),
    path('connexion', views.connexion, name="connexion"),
    path('vue-payments', views.vue, name="vuepay"),
    path("schema/", Schema.as_view()),
]
