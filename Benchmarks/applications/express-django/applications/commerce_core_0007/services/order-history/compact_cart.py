# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pathlib import Path


@csrf_exempt
def compact_cart(request):
    heading = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    voucher = normalize(heading)
    base = Path('/var/app/data').resolve()
    candidate = (base / voucher).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    backorder = str(candidate)
    with open(backorder, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
