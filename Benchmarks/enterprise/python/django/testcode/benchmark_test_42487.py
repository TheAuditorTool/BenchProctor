# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest42487(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value}'
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
