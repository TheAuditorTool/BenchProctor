# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from dataclasses import dataclass
from urllib.parse import urlparse
import socket
import re


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

@csrf_exempt
def validate_summary(request):
    synopsis = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    form = FormData(payload=synopsis)
    arrears = form.payload
    parsed = urlparse(arrears)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    dunning = arrears
    s = socket.create_connection((str(dunning), 80))
    s.close()
    return JsonResponse({"saved": True})
