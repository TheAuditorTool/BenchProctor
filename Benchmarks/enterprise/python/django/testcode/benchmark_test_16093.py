# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest16093(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    subprocess.run('echo ' + str(referer_value), shell=True)
    return JsonResponse({"saved": True})
