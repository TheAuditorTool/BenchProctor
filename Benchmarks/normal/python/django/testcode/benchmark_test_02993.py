# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import urllib.request


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest02993(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
