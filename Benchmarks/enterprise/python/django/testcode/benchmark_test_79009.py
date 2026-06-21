# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest79009(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = coalesce_blank(cookie_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
