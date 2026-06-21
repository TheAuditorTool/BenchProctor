# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest03490(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
