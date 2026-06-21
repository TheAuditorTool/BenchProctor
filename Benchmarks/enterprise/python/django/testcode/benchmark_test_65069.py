# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re
from urllib.parse import unquote


def BenchmarkTest65069(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return JsonResponse({"saved": True})
