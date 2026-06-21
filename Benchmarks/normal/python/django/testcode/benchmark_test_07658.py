# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json


def BenchmarkTest07658(request):
    cookie_value = request.COOKIES.get('session_token', '')
    yaml.safe_load(cookie_value)
    return JsonResponse({"saved": True})
