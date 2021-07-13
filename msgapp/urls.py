from django.urls import path
from . import  views

urlpatterns = [
    path('',views.msgproc),
    path('homeproc1',views.homeproc1),
    path('homeproc2',views.homeproc2),
    path('pgproc',views.pgproc())
]