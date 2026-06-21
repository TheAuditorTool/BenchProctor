# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
import subprocess


def coalesce_blank(value):
    return value or ''

def BenchmarkTest00007(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = coalesce_blank(forwarded_ip)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return JsonResponse({"saved": True})
