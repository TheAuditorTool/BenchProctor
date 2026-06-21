# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
from urllib.parse import unquote
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest25275(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = unquote(field_value)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
