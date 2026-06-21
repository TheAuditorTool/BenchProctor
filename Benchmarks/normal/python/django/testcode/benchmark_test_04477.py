# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import sys


def coalesce_blank(value):
    return value or ''

def BenchmarkTest04477(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = coalesce_blank(argv_value)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
