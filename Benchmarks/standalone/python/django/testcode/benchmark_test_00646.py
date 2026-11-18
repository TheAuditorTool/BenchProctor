# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest00646(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
