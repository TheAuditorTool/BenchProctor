# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pathlib import Path


@csrf_exempt
def prune_config(request):
    footnote = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    consignment = normalize(footnote)
    base = Path('/var/app/data').resolve()
    candidate = (base / consignment).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    parcel = str(candidate)
    with open(parcel, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
