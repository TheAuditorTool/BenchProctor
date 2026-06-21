# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67442(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    int(str(data))
    return JsonResponse({"saved": True})
