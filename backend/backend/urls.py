# import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
# from rest_framework_simplejwt.views import (TokenObtainPairView,
#                                             TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('chat/', include('ws.urls')),

    # path('apiapp/', include('apiapp.urls')),
   
    
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)