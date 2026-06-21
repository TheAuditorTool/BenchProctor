# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import importlib


def BenchmarkTest54288(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
