# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest44755(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value:.200s}'
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
