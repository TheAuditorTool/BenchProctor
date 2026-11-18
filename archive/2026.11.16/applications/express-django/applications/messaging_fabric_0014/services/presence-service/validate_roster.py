# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import json
import socket
import re


@csrf_exempt
def validate_roster(request):
    summary = json.loads(request.body or b'{}').get('payload', '')
    bulletin = summary if summary else 'default'
    parsed = urlparse(bulletin)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    notice = bulletin
    s = socket.create_connection((str(notice), 80))
    s.close()
    return JsonResponse({"saved": True})
