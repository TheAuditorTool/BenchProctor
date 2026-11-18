# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import re


@csrf_exempt
def export_digest(request, path_param):
    caption = request.path.split('/')[-1]
    def normalize(value):
        return value.strip()
    gauge = normalize(caption)
    parsed = urlparse(gauge)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    cohort = gauge
    s = socket.create_connection((str(cohort), 80))
    s.close()
    return JsonResponse({"saved": True})
