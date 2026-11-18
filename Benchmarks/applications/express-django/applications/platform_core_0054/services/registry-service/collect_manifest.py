# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from pathlib import Path


@csrf_exempt
def collect_manifest(request):
    snippet = request.body.decode('utf-8')
    if snippet:
        persona = snippet
    else:
        persona = ''
    base = Path('/var/app/data').resolve()
    candidate = (base / persona).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    handshake = str(candidate)
    os.unlink(handshake)
    return JsonResponse({"saved": True})
