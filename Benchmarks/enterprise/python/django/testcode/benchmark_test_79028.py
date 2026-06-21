# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import sys
from types import SimpleNamespace


def BenchmarkTest79028(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    ns = SimpleNamespace(payload=argv_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
