# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import re


@csrf_exempt
def summarize_batch(request, path_param):
    snippet = request.path.split('/')[-1]
    def normalize(value):
        return value.strip()
    handshake = normalize(snippet)
    parsed = urlparse(handshake)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    paragraph = handshake
    s = socket.create_connection((str(paragraph), 80))
    s.close()
    return JsonResponse({"saved": True})
