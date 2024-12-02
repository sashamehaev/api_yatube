from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('api-token-auth', CatViewSet)
router.register('posts', CatViewSet)
router.register('groups', CatViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('api/v1/', include('api.urls')),
=======
    path('api/v1/', include(router.urls)),
>>>>>>> 5a7231757dce914175a5eda838c9b7213741a056
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
