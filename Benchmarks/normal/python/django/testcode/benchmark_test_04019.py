# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from django import forms
import json


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest04019(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
