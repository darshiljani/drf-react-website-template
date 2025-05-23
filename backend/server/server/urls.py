"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from constants.permissions import InternalIPPermission
from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from utils.env import APP_ENV

urlpatterns = [
    path("admin/", admin.site.urls),
]

if APP_ENV != "prod":
    from drf_yasg import openapi
    from drf_yasg.views import get_schema_view

    schema_view = get_schema_view(
        openapi.Info(
            title="Project API",
            default_version="v1",
            description="Description",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="<your-gmail>@gmail.com"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=[permissions.IsAdminUser, InternalIPPermission],
    )

    dev_urlpatterns = [
        path(
            "doc/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "redoc/",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
        path(
            "json/", schema_view.without_ui(cache_timeout=0), name="schema-json"
        ),
    ]

    urlpatterns += dev_urlpatterns

admin.sites.AdminSite.site_title = "Site Admin"
admin.sites.AdminSite.site_header = "Site Dashboard"
admin.sites.AdminSite.index_title = "Site Admin Panel"
