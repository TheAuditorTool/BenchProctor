# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
import ipaddress
import socket
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest37352(request):
    field_value = UserForm(request.POST).data.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    parsed = urlparse(data)
    resolved = socket.gethostbyname(parsed.hostname or data)
    if ipaddress.ip_address(resolved).is_private:
        return JsonResponse({'error': 'private range blocked'}, status=403)
    target_url = data.replace(parsed.hostname, resolved) if parsed.hostname else data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return JsonResponse({"saved": True})
