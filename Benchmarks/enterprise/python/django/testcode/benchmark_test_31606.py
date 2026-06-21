# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest31606(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '{}'.format(referer_value)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
