# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from app_runtime import auth_check


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest44341(request):
    field_value = UserForm(request.POST).data.get('field', '')
    if not auth_check(str(field_value), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
