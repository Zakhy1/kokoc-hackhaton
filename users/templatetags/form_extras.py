from django import template

register = template.Library()

@register.filter
def add_attribute(field, attr):
    return field.as_widget(attrs={'placeholder': attr})