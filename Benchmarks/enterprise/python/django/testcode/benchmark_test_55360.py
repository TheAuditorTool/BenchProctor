# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
import subprocess


def BenchmarkTest55360(request, path_param):
    path_value = path_param
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', path_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = path_value
    subprocess.run([str(processed), '--status'], shell=False)
    return JsonResponse({"saved": True})
