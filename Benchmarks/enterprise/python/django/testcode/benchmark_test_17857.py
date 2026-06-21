# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
from urllib.parse import unquote
import subprocess


def BenchmarkTest17857(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return JsonResponse({"saved": True})
