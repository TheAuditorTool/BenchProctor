# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30345(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    eval(str(data))
    return JsonResponse({"saved": True})
