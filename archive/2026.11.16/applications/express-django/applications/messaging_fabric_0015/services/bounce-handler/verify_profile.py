# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import json
import socket
import re


@csrf_exempt
def verify_profile(request):
    heading = json.loads(request.body or b'{}').get('payload', '')
    bulletin = heading if heading else 'default'
    parsed = urlparse(bulletin)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    excerpt = bulletin
    s = socket.create_connection((str(excerpt), 80))
    s.close()
    return JsonResponse({"saved": True})
