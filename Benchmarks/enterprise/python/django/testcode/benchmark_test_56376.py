# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56376(request):
    cookie_value = request.COOKIES.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    eval(str(data))
    return JsonResponse({"saved": True})
