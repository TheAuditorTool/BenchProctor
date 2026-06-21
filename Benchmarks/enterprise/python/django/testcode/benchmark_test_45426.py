# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest45426(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
