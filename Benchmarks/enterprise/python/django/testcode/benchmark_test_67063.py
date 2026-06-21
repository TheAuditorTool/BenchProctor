# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import sys


def BenchmarkTest67063(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = '%s' % str(argv_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    with open('/var/app/data/' + str(processed), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
