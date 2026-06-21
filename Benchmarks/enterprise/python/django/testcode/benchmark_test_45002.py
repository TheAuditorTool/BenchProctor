# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import ast


def BenchmarkTest45002(request):
    cookie_value = request.COOKIES.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
