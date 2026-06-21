# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re


def BenchmarkTest10300(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', ua_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = ua_value
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return JsonResponse({"saved": True})
