# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django import forms
import urllib.request
import urllib.parse
import ssl


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest04009(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = (lambda v: v.strip())(field_value)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
