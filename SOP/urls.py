from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("pic.urls")),
    path('', include("user.urls")), #django will check here for 'register' and 'login'.
    #path('', include("django.contrib.auth.urls")), # Make sure that the '' is blank so that there is no repetition of 'login/' search when it is passed into the url search
]
