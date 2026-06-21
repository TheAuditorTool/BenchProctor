# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re
import sys


def BenchmarkTest08377(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = '{}'.format(argv_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
