# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest55237(request):
    field_value = UserForm(request.POST).data.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
