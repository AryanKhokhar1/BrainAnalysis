from django.contrib import admin
from django.urls import path
from analysis import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="Home"),
    path("about",views.about,name="Detail"),
    path("report",views.report,name="Report"),
    path("home",views.home,name="Home")
]