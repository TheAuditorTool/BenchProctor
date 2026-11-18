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
def resolve_bundle(request):
    snippet = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    form = FormData(payload=snippet)
    persona = form.payload
    parsed = urlparse(persona)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    synopsis = persona
    s = socket.create_connection((str(synopsis), 80))
    s.close()
    return JsonResponse({"saved": True})
