from django.urls import path
from contact_app import views

urlpatterns=[
    path("",views.contact_list,name="contact-list"),
    path("delete/<int:pk>/", views.delete_contact, name='delete-contact'),
    path("add/", views.add_contact, name='add-contact'),
    path("edit/<int:pk>/", views.edit_contact, name='edit-contact'),
]
