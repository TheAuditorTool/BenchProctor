# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest23272(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
