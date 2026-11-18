# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import socket
import re


@csrf_exempt
def merge_summary(request):
    transcript = request.META.get('HTTP_X_FORWARDED_FOR', '')
    rendition = (lambda v: v.strip())(transcript)
    parsed = urlparse(rendition)
    resolved = socket.gethostbyname(parsed.hostname or rendition)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return JsonResponse({'error': 'private range blocked'}, status=403)
    montage = rendition
    requests.get(str(montage))
    return JsonResponse({"saved": True})
