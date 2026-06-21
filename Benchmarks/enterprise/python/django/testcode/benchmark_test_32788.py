# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest32788(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
