# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pathlib import Path


def BenchmarkTest00139(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    parts = str(origin_value).split(',')
    data = ' '.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    Path(checked_path).write_text('data')
    return JsonResponse({"saved": True})
