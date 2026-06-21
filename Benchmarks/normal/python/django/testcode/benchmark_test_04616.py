# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest04616(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
