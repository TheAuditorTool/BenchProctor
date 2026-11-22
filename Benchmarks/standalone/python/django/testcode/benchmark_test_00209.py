# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest00209(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = header_value if header_value else 'default'
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
