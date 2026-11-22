# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import urllib.parse
import re


@csrf_exempt
def export_profile(request):
    synopsis = request.META.get('HTTP_ORIGIN', '')
    rendition = (lambda v: v.strip())(synopsis)
    parsed = urlparse(rendition)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", rendition) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    montage = rendition
    s = socket.create_connection((urllib.parse.urlparse(str(montage)).hostname, 80))
    s.close()
    return JsonResponse({"saved": True})
