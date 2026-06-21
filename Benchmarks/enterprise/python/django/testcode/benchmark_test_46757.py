# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import importlib


def BenchmarkTest46757(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
