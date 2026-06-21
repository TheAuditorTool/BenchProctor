# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest58499(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
