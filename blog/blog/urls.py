"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
# from django.contrib import admin
from personal_blog.views import IndexView
from django.views.static import serve
from blog.settings import MEDIA_ROOT
import users
import xadmin
from personal_blog import views
from users import views
import personal_blog.views

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^user/',include('users.urls',namespace='user')),
    # url(r'^user/register/$',views.register,name='register'),
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^article/',include('personal_blog.urls',namespace='article')),
    # url(r'^article/detail/(?P<article_id>\d+)/$',personal_blog.views.detail,name='article_detail'),
    # url(r'^article/recommend/(?P<recommend_id>\d+)/$',personal_blog.views.recommend,name='article_recommend'),
    # url(r'^article/list/(?P<column_id>\d+)/$',personal_blog.views.list,name='list'),
    url(r'^media/(?P<path>.*)$',serve,{'document_root':MEDIA_ROOT}),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
]
