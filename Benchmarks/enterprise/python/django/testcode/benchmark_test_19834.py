# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import base64
import subprocess


def BenchmarkTest19834(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return JsonResponse({"saved": True})
