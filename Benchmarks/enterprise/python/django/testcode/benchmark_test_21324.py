# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re


def BenchmarkTest21324(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(referer_value)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = referer_value
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return JsonResponse({"saved": True})
