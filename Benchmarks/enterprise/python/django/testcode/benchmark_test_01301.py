# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest01301(request):
    cookie_value = request.COOKIES.get('session_token', '')
    os.remove(str(cookie_value))
    return JsonResponse({"saved": True})
