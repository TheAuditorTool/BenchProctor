# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from urllib.parse import urlparse
import requests
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00150(request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    reader = make_reader(api_value)
    data = reader()
    parsed = urlparse(data)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", data) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return redirect(str(target_url))
