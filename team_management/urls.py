from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/team/", include("teams.urls")),
    path("api/member/", include("members.urls")),
]
