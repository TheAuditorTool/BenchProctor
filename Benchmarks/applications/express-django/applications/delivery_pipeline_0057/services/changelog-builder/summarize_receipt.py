# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import re


@csrf_exempt
def summarize_receipt(request, path_param):
    footnote = request.path.split('/')[-1]
    def normalize(value):
        return value.strip()
    wording = normalize(footnote)
    parsed = urlparse(wording)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    note = wording
    s = socket.create_connection((str(note), 80))
    s.close()
    return JsonResponse({"saved": True})
