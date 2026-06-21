# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import ipaddress
import socket
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest00563(request):
    field_value = UserForm(request.POST).data.get('field', '')
    parsed = urlparse(field_value)
    resolved = socket.gethostbyname(parsed.hostname or field_value)
    if ipaddress.ip_address(resolved).is_private:
        return JsonResponse({'error': 'private range blocked'}, status=403)
    target_url = field_value.replace(parsed.hostname, resolved) if parsed.hostname else field_value
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
