# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def ensure_str(value):
    return str(value)

def BenchmarkTest05391(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = ensure_str(header_value)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return JsonResponse({"saved": True})
