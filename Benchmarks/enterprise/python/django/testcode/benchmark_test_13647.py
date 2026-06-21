# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re
import sys
from types import SimpleNamespace


def BenchmarkTest13647(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    ns = SimpleNamespace(payload=argv_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return JsonResponse({"saved": True})
