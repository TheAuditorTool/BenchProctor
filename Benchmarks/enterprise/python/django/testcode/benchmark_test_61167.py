# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest61167(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value}'
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
