# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from urllib.parse import unquote
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest52870(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = unquote(field_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
