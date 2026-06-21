# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import sys


def BenchmarkTest42393(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = str(argv_value).replace('\x00', '')
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.unlink('/var/app/data/' + str(processed))
    return JsonResponse({"saved": True})
