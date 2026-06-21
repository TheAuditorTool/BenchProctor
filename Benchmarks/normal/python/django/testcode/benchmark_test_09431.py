# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest09431(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value}'
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
