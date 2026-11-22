# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest00101(request):
    cookie_value = request.COOKIES.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
