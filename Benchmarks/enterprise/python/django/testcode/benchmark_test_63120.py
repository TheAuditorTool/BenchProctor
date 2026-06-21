# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest63120(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
