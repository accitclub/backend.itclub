from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from itc_backend.apps.core.api.executive_api import ExecutiveRetrieveAPI
from itc_backend.apps.users.api.views import UserRetrieveViewSet


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserRetrieveViewSet)


app_name = "api"
urlpatterns = router.urls
urlpatterns += [
    path("execuitve/", ExecutiveRetrieveAPI.as_view())
]
