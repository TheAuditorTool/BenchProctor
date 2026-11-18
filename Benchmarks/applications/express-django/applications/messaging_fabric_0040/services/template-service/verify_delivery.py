# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import re


@csrf_exempt
def verify_delivery(request, path_param):
    preface = request.path.split('/')[-1]
    def normalize(value):
        return value.strip()
    bulletin = normalize(preface)
    parsed = urlparse(bulletin)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    notice = bulletin
    s = socket.create_connection((str(notice), 80))
    s.close()
    return JsonResponse({"saved": True})
