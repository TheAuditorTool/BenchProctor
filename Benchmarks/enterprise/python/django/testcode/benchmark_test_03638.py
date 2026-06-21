# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re
import sys


def BenchmarkTest03638(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    parts = str(argv_value).split(',')
    data = ','.join(parts)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
