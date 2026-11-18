# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pathlib import Path


@csrf_exempt
def prune_receipt(request):
    transcript = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    rendition = normalize(transcript)
    base = Path('/var/app/data').resolve()
    candidate = (base / rendition).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    montage = str(candidate)
    with open(montage, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
