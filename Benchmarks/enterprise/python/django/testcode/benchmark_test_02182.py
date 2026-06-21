# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest02182(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = f'{header_value:.200s}'
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
