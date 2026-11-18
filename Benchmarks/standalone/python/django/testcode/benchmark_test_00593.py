# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest00593(request):
    cookie_value = request.COOKIES.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ' '.join(parts)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
