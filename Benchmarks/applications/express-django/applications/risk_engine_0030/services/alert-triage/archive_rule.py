# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from pathlib import Path


@csrf_exempt
def archive_rule(request):
    summary = request.body.decode('utf-8')
    if summary:
        grievance = summary
    else:
        grievance = ''
    base = Path('/var/app/data').resolve()
    candidate = (base / grievance).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    verdict = str(candidate)
    os.unlink(verdict)
    return JsonResponse({"saved": True})
