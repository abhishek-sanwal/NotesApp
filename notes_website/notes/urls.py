from django.urls import path

from notes_website.notes import views
from views import *


url_pattern = [
    path('',views.index,name ="notes"),
    path('/delete/<str:item_id>',views.remove, name = "delete"),

]