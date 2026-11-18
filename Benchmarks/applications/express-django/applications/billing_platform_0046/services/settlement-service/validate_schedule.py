# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pathlib import Path


@csrf_exempt
def validate_schedule(request):
    remark = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    remittance = normalize(remark)
    base = Path('/var/app/data').resolve()
    candidate = (base / remittance).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    arrears = str(candidate)
    with open(arrears, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
