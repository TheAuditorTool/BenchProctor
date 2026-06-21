# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
from django import forms
import socket


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def relay_value(value):
    return value

def BenchmarkTest18580(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = relay_value(field_value)
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return JsonResponse({"saved": True})
