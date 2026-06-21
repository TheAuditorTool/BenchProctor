# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from app_runtime import auth_check


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest13864(request):
    field_value = UserForm(request.POST).data.get('field', '')
    auth_check('user', field_value)
    return JsonResponse({"saved": True})
