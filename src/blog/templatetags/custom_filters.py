import markdown

from django.template import Library
from django.utils.safestring import mark_safe

register = Library()


@register.filter(name='as_html')
def markdown_to_html(value):
    """ Converts markdown text to HTML """
    return mark_safe(markdown.markdown(value))