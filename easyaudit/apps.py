from django.apps import AppConfig

class EasyAuditConfig(AppConfig):
    name = 'easyaudit'
    verbose_name = 'Audit Trail'

    def ready(self):
        from easyaudit.signals import auth_signals, model_signals, request_signals