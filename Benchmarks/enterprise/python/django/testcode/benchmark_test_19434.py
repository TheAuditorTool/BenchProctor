# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from types import SimpleNamespace


def BenchmarkTest19434(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    eval(compile("subprocess.run('echo ' + str(data), shell=True)", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
