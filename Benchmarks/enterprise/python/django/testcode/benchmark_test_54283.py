# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64


def BenchmarkTest54283(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
