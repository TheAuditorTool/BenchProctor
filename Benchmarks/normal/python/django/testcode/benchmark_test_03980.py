# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest03980(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = unquote(field_value)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
