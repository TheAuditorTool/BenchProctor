# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest40385(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
