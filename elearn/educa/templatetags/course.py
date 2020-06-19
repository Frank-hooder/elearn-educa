from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()
@register.filter
@stringfilter
def model_name(obj):
	try:
		return obj._meta.module_name
	except AttributeError:
		return None