# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest02392(request):
    field_value = UserForm(request.POST).data.get('field', '')
    processed = 'true' if str(field_value).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
