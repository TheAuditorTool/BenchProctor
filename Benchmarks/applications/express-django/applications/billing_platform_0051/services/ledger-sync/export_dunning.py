# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from pathlib import Path


@csrf_exempt
def export_dunning(request):
    synopsis = request.body.decode('utf-8')
    if synopsis:
        arrears = synopsis
    else:
        arrears = ''
    base = Path('/var/app/data').resolve()
    candidate = (base / arrears).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    dunning = str(candidate)
    os.unlink(dunning)
    return JsonResponse({"saved": True})
