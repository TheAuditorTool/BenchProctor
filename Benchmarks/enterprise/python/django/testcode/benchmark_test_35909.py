# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest35909(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = str(field_value).replace('\x00', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
