# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pathlib import Path


@csrf_exempt
def reconcile_bundle(request):
    summary = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    gauge = normalize(summary)
    base = Path('/var/app/data').resolve()
    candidate = (base / gauge).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    cohort = str(candidate)
    with open(cohort, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
