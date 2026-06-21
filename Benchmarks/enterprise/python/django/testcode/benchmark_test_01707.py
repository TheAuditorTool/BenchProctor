# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from urllib.parse import unquote


def BenchmarkTest01707(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
