# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from urllib.parse import urlparse
import json
import re


def BenchmarkTest00282(request):
    cookie_value = request.COOKIES.get('session_token', '')
    try:
        data = json.loads(cookie_value).get('value', cookie_value)
    except (json.JSONDecodeError, AttributeError):
        data = cookie_value
    parsed = urlparse(data)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return redirect(str(target_url))
