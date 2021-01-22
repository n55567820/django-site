from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('articles/<int:a_id>',views.view_article, name='view_articles'),
    path('articles/create', views.create_article, name='create_article'),
    path('articles/edit/<int:a_id>', views.edit_article , name='edit_article'),
    path('articles/delete/<int:a_id>', views.delete_article, name='delete_article'),
    path('signin', views.signin, name='signin'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
]