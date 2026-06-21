# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07119(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    eval(str(data))
    return JsonResponse({"saved": True})
