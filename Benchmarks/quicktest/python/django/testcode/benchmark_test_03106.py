# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import sys


def relay_value(value):
    return value

def BenchmarkTest03106(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = relay_value(argv_value)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
