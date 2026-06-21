# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest07063(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = ' '.join(str(field_value).split())
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
