from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from wallet.users.views import UserViewSet
from wallet.wallets.views import WalletViewSet
from wallet.clients.views import ClientViewSet


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("wallets", WalletViewSet)
router.register("clients", ClientViewSet)

app_name = "api"
urlpatterns = router.urls
