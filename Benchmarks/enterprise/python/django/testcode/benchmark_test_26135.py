# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from types import SimpleNamespace


def BenchmarkTest26135(request):
    host_value = request.META.get('HTTP_HOST', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    eval(compile("subprocess.run('echo ' + str(data), shell=True)", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
