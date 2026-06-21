# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from urllib.parse import unquote


def BenchmarkTest62720(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
