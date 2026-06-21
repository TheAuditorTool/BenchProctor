# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest48869(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = default_blank(field_value)
    processed = html.escape(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
