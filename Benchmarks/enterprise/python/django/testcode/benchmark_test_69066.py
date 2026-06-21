# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69066(request):
    cookie_value = request.COOKIES.get('session_token', '')
    eval(str(cookie_value))
    return JsonResponse({"saved": True})
