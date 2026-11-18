# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from pathlib import Path


@csrf_exempt
def reconcile_snapshot(request):
    snippet = request.body.decode('utf-8')
    if snippet:
        handshake = snippet
    else:
        handshake = ''
    base = Path('/var/app/data').resolve()
    candidate = (base / handshake).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    paragraph = str(candidate)
    os.unlink(paragraph)
    return JsonResponse({"saved": True})
