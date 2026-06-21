# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest64353(request):
    field_value = UserForm(request.POST).data.get('field', '')
    parsed = urlparse(field_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = field_value
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
