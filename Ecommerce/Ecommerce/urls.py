from django.contrib.auth.views import LogoutView, LoginView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import signup, login2

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    # Users' URLs
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('signup/', signup, name='signup'),
    # Separated Routes
    path('', include('core.urls')),
    path('cart/', include('cart.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
