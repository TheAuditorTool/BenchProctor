# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pathlib import Path


@csrf_exempt
def summarize_reservation(request):
    citation = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    backorder = normalize(citation)
    base = Path('/var/app/data').resolve()
    candidate = (base / backorder).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    restock = str(candidate)
    with open(restock, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
