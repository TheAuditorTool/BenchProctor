# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest01335(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
