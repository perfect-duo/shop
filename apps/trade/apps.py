from django.apps import AppConfig


class TradeConfig(AppConfig):
    name = 'trade'
    verbose_name = "交易"

    def ready(self):
        import trade.signal
