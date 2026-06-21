# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest16071(request):
    field_value = UserForm(request.POST).data.get('field', '')
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
