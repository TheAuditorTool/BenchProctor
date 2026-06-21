# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
from urllib.parse import unquote


def BenchmarkTest24119(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
