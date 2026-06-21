# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def to_text(value):
    return str(value).strip()

def BenchmarkTest59114(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = to_text(field_value)
    request.session.clear()
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
