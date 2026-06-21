# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest77836(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
