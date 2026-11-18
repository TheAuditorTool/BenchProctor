# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from pathlib import Path


@csrf_exempt
def load_batch(request):
    footnote = request.body.decode('utf-8')
    if footnote:
        handshake = footnote
    else:
        handshake = ''
    base = Path('/var/app/data').resolve()
    candidate = (base / handshake).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    blurb = str(candidate)
    os.unlink(blurb)
    return JsonResponse({"saved": True})
