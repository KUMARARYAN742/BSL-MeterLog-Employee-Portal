from django.apps import AppConfig


class ElectricmeterReadingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'electricmeter_reading'

    def ready(self):
        import electricmeter_reading.signals  # Ensure signals are imported
