# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import unquote
import requests
from urllib.parse import urlparse
import re


@csrf_exempt
def render_roster(request):
    caption = request.GET.get('id', '')
    handshake = unquote(caption)
    parsed = urlparse(handshake)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", handshake) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    subject = handshake
    requests.get(str(subject))
    return JsonResponse({"saved": True})
