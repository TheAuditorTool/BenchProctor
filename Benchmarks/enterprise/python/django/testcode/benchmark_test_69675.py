# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re
from urllib.parse import unquote


def BenchmarkTest69675(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return JsonResponse({"saved": True})
