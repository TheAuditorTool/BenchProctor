# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest51696(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
