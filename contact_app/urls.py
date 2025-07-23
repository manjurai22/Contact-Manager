from django.urls import path
from contact_app import views

urlpatterns=[
    path("",views.contact_list,name="contact-list"),
]
