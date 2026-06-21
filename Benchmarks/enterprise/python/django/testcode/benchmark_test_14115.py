# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import base64


def BenchmarkTest14115(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
