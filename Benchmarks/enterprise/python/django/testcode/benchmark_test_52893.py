# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52893(request):
    cookie_value = request.COOKIES.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    int(str(data))
    return JsonResponse({"saved": True})
