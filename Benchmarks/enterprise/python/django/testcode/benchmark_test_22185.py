# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def ensure_str(value):
    return str(value)

def BenchmarkTest22185(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = ensure_str(auth_header)
    processed = data[:64]
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return JsonResponse({"saved": True})
