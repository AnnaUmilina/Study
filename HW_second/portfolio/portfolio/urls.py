from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main import views as v
from authorization import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index, name='index'),
    path('blog/', include('blog.urls')),

    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('home/', views.home, name='home'),

    path('current/', views.currentauthorization, name='currentauthorization'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
