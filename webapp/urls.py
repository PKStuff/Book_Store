from django.urls import path
from . import views

urlpatterns = [
    path('', views.display , name='index'),
    path('upload/', views.upload_file, name='upload_file'),
    path('register/', views.email_validate, name='register'),
    path('email/', views.email_send, name='email'),
    path('review/<int:book_id>/',views.display_review, name='review'),
    path('reviews/<int:book_id>/', views.write_review, name='write_review'),
    path('upload/<str:book_grp_name>/', views.bookgroup, name='bookgroup'),
]