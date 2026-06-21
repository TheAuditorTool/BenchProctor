# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71932(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
