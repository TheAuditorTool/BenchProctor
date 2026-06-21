# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest77258(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
