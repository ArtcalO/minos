
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
#from api_minos.urls import router as mino_router 
from rest_framework import routers

#rout=routers.DefaultRouter()
#rout.registry.extend(mino_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('minos/', include("api_minos.urls")),

]
