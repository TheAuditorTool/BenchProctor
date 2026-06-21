# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05738(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    int(str(data))
    return JsonResponse({"saved": True})
