from django.urls import path
from .views import IndexView,register_request,login_request,PostAddView,PostView,Postdelateview,Postupdateview


urlpatterns = [
    path('', IndexView, name='home'),
    path('register/', register_request, name='register'),
    path('login/', login_request, name='login'),
    path('postadd/', PostAddView, name='postadd'),
    path('post/', PostView, name='post'),
    path('news/update/', Postupdateview.as_view(), name='post_update'),
    path('news/delate/', Postdelateview.as_view(), name='post_delate'),
]