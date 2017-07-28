from django import template

register = template.Library()


@register.simple_tag
def canonical_url(request, relative_url):
    url = request.build_absolute_uri(relative_url)
    return url