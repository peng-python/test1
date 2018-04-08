from django.conf.urls import url
import views


urlpatterns=[
    url(r'register/$',views.register,name='register'),
    url(r'^login/$',views.login_user,name='login'),
    url(r'^logout/$',views.logout_user,name='logout'),
]