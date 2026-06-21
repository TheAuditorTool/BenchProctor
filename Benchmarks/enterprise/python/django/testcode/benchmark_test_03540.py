# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest03540(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if ua_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = ua_value
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
