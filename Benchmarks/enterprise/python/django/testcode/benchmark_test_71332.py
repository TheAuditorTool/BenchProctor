# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re


def BenchmarkTest71332(request):
    user_id = request.GET.get('id', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', user_id):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = user_id
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return JsonResponse({"saved": True})
