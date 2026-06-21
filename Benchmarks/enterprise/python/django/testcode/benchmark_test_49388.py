# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest49388(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
