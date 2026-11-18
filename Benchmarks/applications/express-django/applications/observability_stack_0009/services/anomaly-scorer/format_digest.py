# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from pathlib import Path


@csrf_exempt
def format_digest(request):
    summary = request.body.decode('utf-8')
    if summary:
        gauge = summary
    else:
        gauge = ''
    base = Path('/var/app/data').resolve()
    candidate = (base / gauge).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    cohort = str(candidate)
    os.unlink(cohort)
    return JsonResponse({"saved": True})
