from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TransfersConfig(AppConfig):
    name = "wallet.transfers"
    verbose_name = _("Transfers")
