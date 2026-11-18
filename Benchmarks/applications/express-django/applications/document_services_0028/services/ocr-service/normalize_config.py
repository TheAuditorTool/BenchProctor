# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import re


@csrf_exempt
def normalize_config(request, path_param):
    note = request.path.split('/')[-1]
    def normalize(value):
        return value.strip()
    addendum = normalize(note)
    parsed = urlparse(addendum)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    dossier = addendum
    s = socket.create_connection((str(dossier), 80))
    s.close()
    return JsonResponse({"saved": True})
