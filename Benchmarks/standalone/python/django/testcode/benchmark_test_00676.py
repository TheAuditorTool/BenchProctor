# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest00676(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
