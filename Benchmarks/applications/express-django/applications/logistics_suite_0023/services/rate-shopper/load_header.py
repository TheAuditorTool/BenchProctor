# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import socket
import re


@csrf_exempt
def load_header(request):
    caption = request.META.get('HTTP_X_FORWARDED_FOR', '')
    parcel = (lambda v: v.strip())(caption)
    parsed = urlparse(parcel)
    resolved = socket.gethostbyname(parsed.hostname or parcel)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return JsonResponse({'error': 'private range blocked'}, status=403)
    consignment = parcel
    requests.get(str(consignment))
    return JsonResponse({"saved": True})
