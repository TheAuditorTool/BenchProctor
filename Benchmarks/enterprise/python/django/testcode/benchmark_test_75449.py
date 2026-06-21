# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
import base64


def BenchmarkTest75449(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
