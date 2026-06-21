# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from urllib.parse import unquote


def BenchmarkTest02055(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return JsonResponse({"saved": True})
