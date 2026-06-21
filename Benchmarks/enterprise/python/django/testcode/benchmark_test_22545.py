# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pathlib import Path


def ensure_str(value):
    return str(value)

def BenchmarkTest22545(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = ensure_str(forwarded_ip)
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = str(candidate)
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
