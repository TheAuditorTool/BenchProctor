# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import re


@csrf_exempt
def enrich_threshold(request):
    synopsis = request.COOKIES.get('session_token', '')
    kind = 'json' if str(synopsis).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            byline = str(synopsis).strip()
        case _:
            byline = str(synopsis)
    parsed = urlparse(byline)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    addendum = byline
    s = socket.create_connection((str(addendum), 80))
    s.close()
    return JsonResponse({"saved": True})
