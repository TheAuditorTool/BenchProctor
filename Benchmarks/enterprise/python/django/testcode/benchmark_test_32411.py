# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest32411(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = unquote(field_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
