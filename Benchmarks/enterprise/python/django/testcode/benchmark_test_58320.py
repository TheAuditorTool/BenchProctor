# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from urllib.parse import unquote


def BenchmarkTest58320(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
