# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from urllib.parse import unquote


def BenchmarkTest23379(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
