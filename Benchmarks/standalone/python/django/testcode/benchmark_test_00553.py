# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from urllib.parse import urlparse
import requests
import re


def BenchmarkTest00553(request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    if api_value:
        data = api_value
    else:
        data = ''
    parsed = urlparse(data)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return redirect(str(target_url))
