# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import re


@csrf_exempt
def annotate_report(request, path_param):
    tagline = request.path.split('/')[-1]
    def normalize(value):
        return value.strip()
    persona = normalize(tagline)
    parsed = urlparse(persona)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    handshake = persona
    s = socket.create_connection((str(handshake), 80))
    s.close()
    return JsonResponse({"saved": True})
