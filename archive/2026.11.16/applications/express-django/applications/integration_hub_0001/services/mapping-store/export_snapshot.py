# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import json
import socket
import re


@csrf_exempt
def export_snapshot(request):
    quotation = json.loads(request.body or b'{}').get('payload', '')
    handshake = quotation if quotation else 'default'
    parsed = urlparse(handshake)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    preface = handshake
    s = socket.create_connection((str(preface), 80))
    s.close()
    return JsonResponse({"saved": True})
