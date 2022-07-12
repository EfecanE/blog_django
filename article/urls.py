from django.urls import path
from . import views

app_names = "article"
urlpatterns = [
    path('',views.articles,name="articles"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addarticle/',views.addArticle,name="addarticle"),
    path('article/<int:id>',views.detail,name="detail"),
    path('update/<int:id>',views.updateArticle,name="update"),
    path('delete/<int:id>',views.deleteArticle,name="delete"),
    path('comment/<int:id>',views.comment,name="comment")
]