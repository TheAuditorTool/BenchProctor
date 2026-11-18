# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pathlib import Path


@csrf_exempt
def audit_roster(request):
    synopsis = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    handshake = normalize(synopsis)
    base = Path('/var/app/data').resolve()
    candidate = (base / handshake).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    memo = str(candidate)
    with open(memo, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
