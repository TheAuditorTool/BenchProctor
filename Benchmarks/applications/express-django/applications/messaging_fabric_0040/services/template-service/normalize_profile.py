# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from pathlib import Path


@csrf_exempt
def normalize_profile(request):
    preface = request.body.decode('utf-8')
    if preface:
        bulletin = preface
    else:
        bulletin = ''
    base = Path('/var/app/data').resolve()
    candidate = (base / bulletin).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    notice = str(candidate)
    os.unlink(notice)
    return JsonResponse({"saved": True})
