# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pathlib import Path
from django.http import HttpResponse


def BenchmarkTest00248(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value!s}'
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = str(candidate)
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
