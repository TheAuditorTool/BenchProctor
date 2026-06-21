# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from types import SimpleNamespace


def BenchmarkTest69281(request):
    raw_body = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    processed = data[:64]
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return JsonResponse({"saved": True})
