# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from urllib.parse import urlparse
import re


def BenchmarkTest00096(request):
    raw_body = request.body.decode('utf-8')
    kind = 'json' if str(raw_body).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(raw_body).strip()
        case _:
            data = str(raw_body)
    parsed = urlparse(data)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return redirect(str(target_url))
