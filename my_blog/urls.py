from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.post_create,name='create'),
    path('',views.post_list,name='list'),
    path('detail/<int:post_id>/',views.post_detail,name='detail'),
    path('update/<int:post_id>/',views.post_update,name='update'),
    path('delete/<int:post_id>/',views.post_delete,name='delete'),

    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view,name='logout'),
]