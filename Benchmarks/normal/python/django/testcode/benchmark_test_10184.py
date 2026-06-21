# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from app_runtime import auth_check


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest10184(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = (lambda v: v.strip())(field_value)
    if auth_check('user', str(data)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
