from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main),
    path('scholarship/', views.scholarship),
    path('scholarship/scholarship1/', views.scholarship1),
    path('scholarship/scholarship2/', views.scholarship2),
    path('schedule/', views.schedule),
    path('job/', views.job),
    path('activity/', views.activity),
    path('blog/', views.list, name="blog"),
    path('blog/post/', views.post),
    path('post',views.post),
    path('post/<int:id>', views.detail, name="detail"),
]