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
def fetch_window(request):
    subject = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    form = FormData(payload=subject)
    grievance = form.payload
    parsed = urlparse(grievance)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    verdict = grievance
    s = socket.create_connection((str(verdict), 80))
    s.close()
    return JsonResponse({"saved": True})
