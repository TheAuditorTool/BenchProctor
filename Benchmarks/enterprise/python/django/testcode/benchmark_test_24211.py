# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest24211(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    subprocess.run(['echo', header_value], shell=False)
    return JsonResponse({"saved": True})
