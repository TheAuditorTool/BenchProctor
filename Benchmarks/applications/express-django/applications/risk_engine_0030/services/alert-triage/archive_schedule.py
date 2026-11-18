# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import socket
import re


@csrf_exempt
def archive_schedule(request):
    summary = request.META.get('HTTP_X_FORWARDED_FOR', '')
    grievance = (lambda v: v.strip())(summary)
    parsed = urlparse(grievance)
    resolved = socket.gethostbyname(parsed.hostname or grievance)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return JsonResponse({'error': 'private range blocked'}, status=403)
    verdict = grievance
    requests.get(str(verdict))
    return JsonResponse({"saved": True})
