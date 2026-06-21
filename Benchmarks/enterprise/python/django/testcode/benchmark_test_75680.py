# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import base64


def BenchmarkTest75680(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    os.remove(str(data))
    return JsonResponse({"saved": True})
