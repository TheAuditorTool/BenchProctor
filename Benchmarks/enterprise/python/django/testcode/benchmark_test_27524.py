# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest27524(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    processed = html.escape(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
