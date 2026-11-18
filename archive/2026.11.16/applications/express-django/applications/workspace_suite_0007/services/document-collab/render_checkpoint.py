# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import json
import socket
import re


@csrf_exempt
def render_checkpoint(request):
    summary = json.loads(request.body or b'{}').get('payload', '')
    subtitle = summary if summary else 'default'
    parsed = urlparse(subtitle)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    notice = subtitle
    s = socket.create_connection((str(notice), 80))
    s.close()
    return JsonResponse({"saved": True})
