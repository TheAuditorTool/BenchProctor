# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import urllib.request
import urllib.parse
import ssl


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest44132(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = ' '.join(str(field_value).split())
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
