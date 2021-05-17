from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('django_uicomponent.html')
def component(component_name, *args, **kwargs):
    template = f'{settings.COMPONENTS_DIR}/{component_name}'
    return {'UICOMPONENT_TEMPLATE_NAME': template, **kwargs }
