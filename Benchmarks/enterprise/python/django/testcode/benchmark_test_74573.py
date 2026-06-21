# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest74573(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = default_blank(field_value)
    json.loads(data)
    return JsonResponse({"saved": True})
