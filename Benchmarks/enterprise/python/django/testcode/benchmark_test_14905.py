# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest14905(request):
    raw_body = request.body.decode('utf-8')
    subprocess.run('echo ' + str(raw_body), shell=True)
    return JsonResponse({"saved": True})
