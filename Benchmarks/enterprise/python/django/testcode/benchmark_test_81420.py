# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def normalise_input(value):
    return value.strip()

def BenchmarkTest81420(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = normalise_input(field_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
