from django.contrib import admin
from django.urls import path, include
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListProducts.as_view(), name='home'),
    path('__debug__/', include("debug_toolbar.urls"))
]
