# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import urllib.request


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest52688(request):
    field_value = UserForm(request.POST).data.get('field', '')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(field_value)).read()
    return JsonResponse({"saved": True})
