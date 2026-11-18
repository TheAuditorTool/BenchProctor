# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from urllib.parse import urlparse
import re


def BenchmarkTest00420(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % str(cookie_value)
    parsed = urlparse(data)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return redirect(str(target_url))
