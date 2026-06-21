# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest23505(request):
    raw_body = request.body.decode('utf-8')
    subprocess.Popen('echo ' + str(raw_body), shell=True).wait()
    return JsonResponse({"saved": True})
