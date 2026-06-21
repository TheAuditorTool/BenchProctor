# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def ensure_str(value):
    return str(value)

def BenchmarkTest31827(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = ensure_str(host_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
