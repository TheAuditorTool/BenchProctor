# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pathlib import Path


@csrf_exempt
def rotate_threshold(request):
    caption = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    ledger = normalize(caption)
    base = Path('/var/app/data').resolve()
    candidate = (base / ledger).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    remittance = str(candidate)
    with open(remittance, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
