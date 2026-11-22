# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest00015(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
