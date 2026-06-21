# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest80790(request):
    field_value = UserForm(request.POST).data.get('field', '')
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
