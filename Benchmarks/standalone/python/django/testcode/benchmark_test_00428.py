# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest00428(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
