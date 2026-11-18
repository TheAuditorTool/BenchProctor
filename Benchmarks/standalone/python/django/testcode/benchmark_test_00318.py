# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re


def BenchmarkTest00318(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
