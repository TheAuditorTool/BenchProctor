# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest60242(request):
    cookie_value = request.COOKIES.get('session_token', '')
    yaml.load(cookie_value, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
