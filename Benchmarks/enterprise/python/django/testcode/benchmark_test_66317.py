# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pathlib import Path


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest66317(request):
    xml_value = request.body.decode('utf-8')
    data = default_blank(xml_value)
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = str(candidate)
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
