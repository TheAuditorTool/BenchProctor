# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from pathlib import Path


@csrf_exempt
def publish_report(request):
    synopsis = request.body.decode('utf-8')
    if synopsis:
        verdict = synopsis
    else:
        verdict = ''
    base = Path('/var/app/data').resolve()
    candidate = (base / verdict).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    grievance = str(candidate)
    os.unlink(grievance)
    return JsonResponse({"saved": True})
