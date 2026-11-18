# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pathlib import Path


@csrf_exempt
def summarize_checkpoint(request):
    note = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    inquiry = normalize(note)
    base = Path('/var/app/data').resolve()
    candidate = (base / inquiry).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    grievance = str(candidate)
    with open(grievance, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
