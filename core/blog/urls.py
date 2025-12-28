# blog/urls.py
from blog import views
from blog.views import root_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # '' means root URL
    path('', root_view),  # <-- This makes http://127.0.0.1:8000/ work
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]
