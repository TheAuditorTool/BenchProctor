# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest11259(request):
    field_value = UserForm(request.POST).data.get('field', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(field_value), secure=True, httponly=True, samesite='Strict')
    return resp
