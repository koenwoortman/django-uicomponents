from django.conf import settings

if not hasattr(settings, 'COMPONENTS_DIR'):
    settings.COMPONENTS_DIR = 'components'
