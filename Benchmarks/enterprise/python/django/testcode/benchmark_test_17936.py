# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest17936(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = '{}'.format(field_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
