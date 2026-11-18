# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from pathlib import Path


@csrf_exempt
def export_window(request):
    transcript = request.body.decode('utf-8')
    if transcript:
        rendition = transcript
    else:
        rendition = ''
    base = Path('/var/app/data').resolve()
    candidate = (base / rendition).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    montage = str(candidate)
    os.unlink(montage)
    return JsonResponse({"saved": True})
