"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import xadmin
from django.urls import re_path, include
from rest_framework.documentation import include_docs_urls
from django.views.static import serve
from shop.settings import MEDIA_ROOT, STATIC_ROOT
urlpatterns = [
    re_path('xadmin/', xadmin.site.urls),
    re_path(r'^media/(?P<path>.*)/$', serve, {"document_root": MEDIA_ROOT}),
    re_path(r'docs/', include_docs_urls(title="多多")),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    re_path(r"goods/", include("goods.urls")),
    re_path(r"users/", include("users.urls")),
    re_path(r"users_operation/", include("user_operation.urls")),
    re_path(r"trade/", include("trade.urls")),
    re_path('', include('social_django.urls', namespace='social')),
    re_path(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT})

]
