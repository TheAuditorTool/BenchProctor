# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest09446(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    reader = make_reader(ua_value)
    data = reader()
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return JsonResponse({"saved": True})
