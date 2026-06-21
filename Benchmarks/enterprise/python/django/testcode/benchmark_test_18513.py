# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18513(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    eval(str(data))
    return JsonResponse({"saved": True})
