# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest20386(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if header_value:
        data = header_value
    else:
        data = ''
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
