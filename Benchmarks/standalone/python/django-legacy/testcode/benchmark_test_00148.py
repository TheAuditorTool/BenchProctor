# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest00148(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = '{}'.format(header_value)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
