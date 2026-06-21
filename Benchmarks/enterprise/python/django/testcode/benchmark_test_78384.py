# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78384(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    int(str(data))
    return JsonResponse({"saved": True})
