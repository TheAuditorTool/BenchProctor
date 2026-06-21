# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from app_runtime import auth_check


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest29563(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = '{}'.format(field_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
