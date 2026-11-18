# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from pathlib import Path


@csrf_exempt
def archive_snapshot(request):
    caption = request.body.decode('utf-8')
    if caption:
        parcel = caption
    else:
        parcel = ''
    base = Path('/var/app/data').resolve()
    candidate = (base / parcel).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    consignment = str(candidate)
    os.unlink(consignment)
    return JsonResponse({"saved": True})
