# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest33666(request):
    field_value = UserForm(request.POST).data.get('field', '')
    if not str(field_value).isdigit():
        raise ValueError('invalid input: ' + str(field_value))
    return JsonResponse({"saved": True})
